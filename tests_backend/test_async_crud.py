import pytest
from fastapi import status
import httpx


@pytest.mark.asyncio
class TestCreateProducts:
    
    async def test_missing_required_fields(self, logged_in_client: httpx.AsyncClient):
        payload = dict(sku="TEST-90", 
                        # description="TEST-99 Missing Fields", 
                        # hs_code="3404-9010", 
                        package_dimensions="24x24x35", 
                        product_weight_lbs=425.0, 
                        gross_weight_lbs=455.0)

        resp = await logged_in_client.post("/create_product", json=payload)
        assert resp.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


    async def test_missing_default_fields(self, logged_in_client: httpx.AsyncClient):
        payload = dict(sku="TEST-91", 
                        description="TEST-91 Missing Optional Fields", 
                        hs_code="3404-9090", 
                        package_dimensions="24x24x35", 
                        product_weight_lbs=425.0, 
                        gross_weight_lbs=455.0)

        resp = await logged_in_client.post("/create_product", json=payload)
        assert resp.status_code == status.HTTP_200_OK


@pytest.mark.asyncio
class TestCreateShipto:

    async def test_create_shipto(self, logged_in_client: httpx.AsyncClient):

        payload = dict(
                name='Jason Bourne',
                company_name='C.I.A.',
                country='USA',
                state_province='Virginia',
                city_name='Langley',
                unit_number='12',
                street_name='wodward',
                street_type='St',
                phone='221-333-2133',
                email='jason@cia.gov',
                tax_shipping_code='221',
                zip_code='22111')

        resp = await logged_in_client.post("/create_shipto", json=payload)
        assert resp.status_code == status.HTTP_200_OK


    async def test_missing_required_shipto_fields(self, logged_in_client: httpx.AsyncClient):

        payload = dict(
                name='Jason Bourne',
                company_name='C.I.A.',
                country='USA',
                state_province='Virginia',
                city_name='Langley',
                unit_number='12',
                # street_name='wodward',
                # street_type='St',
                phone='221-333-2133',
                email='jason@cia.gov',
                tax_shipping_code='221',
                zip_code='22111')

        resp = await logged_in_client.post("/create_shipto", json=payload)
        assert resp.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


@pytest.mark.asyncio
class TestReadProducts:
    
    async def test_list_products(self, logged_in_client: httpx.AsyncClient):
        resp = await logged_in_client.get("/read/list_products")
        assert resp.status_code == status.HTTP_200_OK
        assert resp.status_code != status.HTTP_404_NOT_FOUND

    async def test_read_all_products_authentication(self, logged_out_client: httpx.AsyncClient):
        r = await logged_out_client.get(f'/read/all_products')
        assert r.status_code == 401

    async def test_read_all_active_products(self, logged_in_client: httpx.AsyncClient):
        r = await logged_in_client.get(f'/read/all_products?isActive=1')
        assert r.status_code == 200
        assert len(r.json()) > 10

    async def test_v2_crud_read_all_active_products_error(self, logged_in_client: httpx.AsyncClient, new_settings):
        err_msg = new_settings.READ_ALL_PROD_ERR
        r = await logged_in_client.get(f'/read/all_products?isActive=3')
        assert r.status_code == 400
        assert r.json()['detail']['message'] == err_msg


    async def test_read_single_product_good_sku(self, logged_in_client: httpx.AsyncClient, good_product_sku):
        sku = good_product_sku
        r = await logged_in_client.get(f'/read/single_product/{sku}')
        assert r.status_code == 200
        assert len(r.json()) > 10

    async def test_read_single_product_bad_sku(self, logged_in_client: httpx.AsyncClient, bad_product_sku, new_settings):
        sku = bad_product_sku
        err_msg = new_settings.READ_SINGLE_PROD_ERR
        r = await logged_in_client.get(f'/read/single_product/{sku}')
        assert r.status_code == 400
        assert r.json()['detail']['message'] == err_msg
    
    async def test_read_single_product_good_sku_no_auth(self, logged_out_client: httpx.AsyncClient, good_product_sku, new_settings):
        sku = good_product_sku
        err_msg = new_settings.READ_SINGLE_PROD_ERR
        r = await logged_out_client.get(f'/read/single_product/{sku}')
        assert r.status_code != 200
        # assert r.json()['detail'] == "LOGIN_USER_NOT_VERIFIED" or r.json()['detail'] == "LOGIN_BAD_CREDENTIALS"






@pytest.mark.asyncio
class TestShipToCRUD:
    
    '''READ - ALL SHIPTO'''
    async def test_v2_crud_read_all_shipto(self, logged_in_client: httpx.AsyncClient):
        r = await logged_in_client.get(f'/read/all_shipto')

        assert r.status_code == 200
        assert len(r.json()) > 1

    '''READ - SINGLE SHIPTO'''
    async def test_v2_crud_read_single_shipto_good_id(self, logged_in_client: httpx.AsyncClient, good_shipto_id):
        id = good_shipto_id
        r = await logged_in_client.get(f'/read/single_shipto/{id}')
        assert r.status_code == 200

    async def test_v2_crud_read_single_shipto_bad_id(self, logged_in_client: httpx.AsyncClient, bad_shipto_id, new_settings):
        bad_id = bad_shipto_id
        oid_err_msg = new_settings.OID_ERROR
        r = await logged_in_client.get(f'/read/single_shipto/{bad_id}')

        assert r.status_code == 400
        assert r.json()['detail']['message'] == oid_err_msg
    

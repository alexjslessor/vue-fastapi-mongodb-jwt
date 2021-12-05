from fastapi import (APIRouter, 
                     Depends, 
                     HTTPException,
                     status)
from bson import ObjectId
from ....config.fastapi_users import fastapi_users
from ....config.config import get_settings
from ....db.schemas import User, CollectionName
from ....db.conn import db
from ....funcs.json_responses import (error_400, 
                                      exception_400,
                                      json_resp_success_200)
settings = get_settings()
router = APIRouter()


@router.delete("/delete/{collection_name}/{id}", 
                response_description='Delete a single document from a collection.')
async def delete_document_by_id(collection_name: CollectionName, 
                                id: str,
                                current_user: User = Depends(fastapi_users.current_user())):
    
    if not ObjectId.is_valid(id):
        return exception_400(settings.OID_ERROR, 
                             'red')

    if collection_name.value == 'products':
        print('product delete id: ', id)
        # delete_result = await db["Products"].delete_one({"_id": ObjectId(oid=id)})
        # if delete_result.deleted_count == 1:
        return json_resp_success_200('Product Deleted', 
                                         'green')

    elif collection_name.value == 'shipto':
        delete_result = await db["ShipTo"].delete_one({"_id": ObjectId(oid=id)})
        if delete_result.deleted_count == 1:
            return json_resp_success_200('Shipping Address Deleted', 
                                         'green')

    # elif collection_name.value == 'orders':
        # print('Deleted Order')
        # delete_result = await db["Order"].delete_one({"_id": ObjectId(oid=id)})
        # if delete_result.deleted_count == 1:
        # return json_resp_success_200('Order Deleted', 
                                    #  'green')

    return exception_400('Record not found.', 
                        'yellow')


# class CollectionName(str, Enum):
#     products = "products"
#     # shipto = "shipto"
#     # orders = "orders"

# @router.post("/delete/{collection_name}/{doc_id}")
# async def delete_document_by_id(collection_name: CollectionName,
#                                 doc_id: str, 
#                                 current_user: User = Depends(fastapi_users.current_user())):
#     try:
#         # bson ObjectId must be 12 or 24 length
#         assert len(doc_id) == 12 or len(doc_id) == 24
#         # assert isinstance(ObjectId(oid=doc_id), ObjectId)
#     except Exception as e:
#         print(e)
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
#                             detail=f"Delete action unavailable, please contact your administrator.")
                    
#     if collection_name == CollectionName.products:      
#         Products.objects(id=doc_id).delete()
    
#     return JSONResponse(status_code=status.HTTP_200_OK, 
#                         content={"message": f'Deleted: {doc_id}'})
  
# # @router.delete("/delete/{collection_name}/{doc_id}")
# # async def delete_document_by_id(collection_name: CollectionName,
# #                                 doc_id: str,
# #                                 current_user: User = Depends(fastapi_users.current_user())
# #                                 ):
# #     delete_result = await db[f"{collection_name}"].delete_one({"_id": id})
# #     if delete_result.deleted_count == 1:
# #         return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
# #     raise HTTPException(status_code=404, detail=f"doc {doc_id} not found")

# @app.delete("/{id}", response_description="Delete a student")
# async def delete_student(id: str):
#     delete_result = await db["students"].delete_one({"_id": id})

#     if delete_result.deleted_count == 1:
#         return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

#     raise HTTPException(status_code=404, detail=f"Student {id} not found")
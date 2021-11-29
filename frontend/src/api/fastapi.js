import axios from "axios";
// import axiosInstance from '../axiosConfig'
// import axiosReq from '../axiosReq'
// import router from '../router'
// import store from '../store'

const axiosReq = axios.create({
    baseURL: process.env.VUE_APP_URL,
    headers: {
      'Authorization': `Bearer ${window.localStorage.getItem('accessToken')}` 
    }
  })

export default {

    async get_Pdf_Document_Fastapi(event) {
        const url = `/${event.invoice_num}/doc/${event.document}.pdf`;
        // let get_doc = await axios.get(url, { withCredentials: true, responseType: 'blob' }
        await axios.get(url, { responseType: 'blob' })
        .then(response => {
            let fileURL = window.URL.createObjectURL(new Blob([response.data]));
            let fileLink = document.createElement('a');
            fileLink.href = fileURL;
            fileLink.setAttribute('download', `${event.invoice_num}-${event.document}.pdf`);
            document.body.appendChild(fileLink);
            fileLink.click();
          });
    },

    async getShipToFastApi(optional) {
        let url = `/get_shipto/${optional.optional}`;
        if (optional.optional === 'all') {
            return await axiosInstance.get(url);
        } else {
            // url = url + '/optional';
            return await axiosInstance.get(url);
            // return await axiosInstance.get(url, optional);
        }
    },



    // SHIPMENT
    async get_Shipment_Que_FastApi() {
        // get_Dashboard_Shipment_Que_Addrs_Api
        const url = `/shipment/get_que_by_address`;
        return await axiosInstance.get(url);
    },
    async post_Shipment_Item_FastApi(event) {
        const url = `/shipment/post_ship_addr`;
        return await axiosInstance.post(url, {event});
    },
    async post_Checkout_Shipment_FastApi(event) {
        // Creates shipment on checkout shipment page
        const url = `/shipment/checkout_shipment`;
        return await axiosInstance.post(url, {event});
    },
    async get_Closed_Orders_FastApi(wo_status) {
        const url = `/shipment/get_closed_orders/${wo_status}`;
        return await axiosInstance.get(url);
    },
    async post_Update_InvoiceNum_FastApi(event) {
        // post_Update_InvoiceNum
        const url = `/shipment/update_invoice_num/${event.invoice_num}/${event.status}`;
        return await axiosInstance.post(url);
    },




    async postCheckoutCartFastApi(cart_items) {
        // const url = `/shop/order_checkout`;
        const url = `/shop/cart-checkout-session`;
        await axiosReq.post(url, {cart_items});
    },



    async get_Dashboard_Que_FastApi() {
        const url = `/get_que`;
        return await axiosReq.get(url);
        // return await axiosReq({ requiresAtuh: true }).get(url);
    },
    async post_Dashboard_QueItem_FastApi(event) {
        const url = `/get_que_item`;
        return await axiosInstance.post(url, event);
    },



    postImageFormFastApi(image_file) {
        // const url = `/uploadfile`;
        const url = `/uploadform`;
        const img = image_file.event;
        const sku = image_file.sku;
        Array.from(img).map(image => {
        // Array.from(image_file).map(image => {
            const file = new FormData();
            file.append('file', image);
            file.append('sku', sku);
            // console.log(file);
            return axiosInstance.post(url, file);
        });
    },

    async updateFromJSONFastAPI(data) {
        console.log('update Collection DocumentFASTAPI: ', data);
        // const url = `/update_from_json/${data.collection}`;
        // const item = {event: data.event}
        // return await axiosInstance.put(url, {item});
        const url = `/update_from_json`;
        const event = {event: data.event, collection: data.collection}
        return await axiosInstance.post(url, {event});
    },
    
    async post_Update_QueItem_FastApi(event) {
        // post_Update_QueItem_Api
        const url = `/update_que`;
        return await axiosInstance.post(url, {event});
    },

}

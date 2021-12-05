from fastapi.responses import JSONResponse
from fastapi import (APIRouter, 
                     Depends, 
                     Body,
                     HTTPException,
                     status)


from ....config.fastapi_users import fastapi_users
from ....config.config import get_settings
from ....config.config_email import get_email_config
from ....db.schemas import (User, ReadProduct, UpdateProduct)
from ....db.conn import db
from ....mongodb_aggregations import *
from ....funcs.json_responses import (exception_400,
                                      error_400,
                                      json_resp_success_200)
# from enum import Enum
from typing import Dict, Optional, Any
# from pydantic import BaseModel
# from datetime import datetime
from bson import ObjectId
from fastapi.encoders import jsonable_encoder
from json import dumps, loads

settings = get_settings()
router = APIRouter()


@router.get("/read/aggregation/{aggregationName}", 
            response_description='Order Table Aggregations')
async def order_aggregations(aggregationName: str,
                            current_user: User = Depends(fastapi_users.current_user())):

    if aggregationName == 'order_que':
        not_lst = ['Complete', 'Cancelled', 'Shipped', 'Reconcile']
        
        a = dashboard_que_agg(status_not_lst=not_lst)
        agg = db['Order'].aggregate(a)
        # agg = await db['Order'].aggregate(dashboard_que_agg(status_not_lst=not_lst))
        print('agg: ', agg)
        results = [str(raw_agg) async for raw_agg in agg]
        # results = dumps([i for i in agg], default=str)

        # print('results: ', results)
        return results
        # if agg:
            # return agg
        # lst = []
        # async for i in agg:
            # print(i)
            # lst.append(i)
        # return lst

    # return exception_400(settings.READ_ALL_PROD_ERR, 'red')
    return exception_400('Aggregation Error: ', 'red')

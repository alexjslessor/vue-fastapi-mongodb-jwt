from starlette.responses import JSONResponse
from starlette.requests import Request
from fastapi.responses import RedirectResponse, FileResponse, JSONResponse
from fastapi.encoders import jsonable_encoder

from fastapi import (APIRouter,
                     Depends,
                     BackgroundTasks,
                     HTTPException)

from fastapi import (status,
                     File, 
                     UploadFile, 
                     Form, 
                     Request,
                     Body)

from typing import Optional, List
# from orjson import loads, dumps
from enum import Enum
import tempfile
import base64
from pydantic import BaseModel
from fastapi import HTTPException, APIRouter
from bson import ObjectId

from ....config.fapi_users import fastapi_users
from ....config.config import get_settings
from ....utils import Utils
from ....apis.deps import *
from ....db.schemas import User, PostsModel, PyObjectId
from ....db.conn import db

router = APIRouter()
settings = get_settings()
# https://pymongo.readthedocs.io/en/stable/api/gridfs/index.html


@router.get("/blog/query_db/{query}/{filter}", response_model=List[PostsModel])
async def read_all_posts():
    p = await db["Posts2"].find().to_list(1000)
    return p


@router.get("/single_post/{id}", response_model=PostsModel)
async def read_post_by_id(id: PyObjectId):
    if (p := await db["Posts2"].find_one({'_id': id})) is not None:
        return p
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                        detail=f"Post {id} not found")


@router.post("/post_blog_form")
async def create_post(
    title: str = Form(...),
    headline: str = Form(...),
    # headline_image: str = Form(...),
    headline_image: UploadFile = File(...), 
    content: str = Form(...)
    ):

    print('title: ', title)
    print('headline: ', headline)
    print('image: ', headline_image.filename)
    print('content: ', content)
    
    
    _img = base64.b64encode(headline_image.file.read())
    # print(_img)
    
    jd = {'title': title, 
          'headline': headline,
          'post_image_bytes': _img,
          'post_image_content_type': headline_image.content_type,
          'content': content
          }

    newPost = jsonable_encoder(jd)
        
    new_post = await db["Posts2"].insert_one(newPost)

    post = await db["Posts2"].find_one({"_id": new_post.inserted_id})    

    return JSONResponse(status_code=status.HTTP_201_CREATED, content='Post created')


# @router.post("/post_blog_form", response_model=PostsModel)
# async def create_post(newBlogPost: Optional[PostsModel] = Body(...),
#                     #   headline_image: Optional[UploadFile] = File(...)
#                       ):
#     # print(newBlogPost)
#     # print(headline_image)
#     newPost = jsonable_encoder(newBlogPost)
#     print(newPost)
    # new_post = await db["Posts"].insert_one(newPost)
    # post = await db["Posts"].find_one({"_id": new_post.inserted_id})
    # return JSONResponse(status_code=status.HTTP_201_CREATED, content=post)


# @router.post("/post_blog_form")
# def blog(title: str = Form(...),
#          headline: str = Form(...),
#          image: UploadFile = File(...), 
#          imageList: List[UploadFile] = File(...),
#          content: str = Form(...)):
    
    # print('title: ', title)
    # print('headline: ', headline)
    # print('image: ', image)
    # print('image list: ', {"filenames": [file.filename for file in imageList]})
    # print('content: ', content)
    
#     post = Posts()
#     post.title = title
#     post.headline = headline
#     post.content = content
    
#     image_str = image.file.read()
#     with tempfile.TemporaryFile() as fp:
#         fp.write(image_str)
#         fp.seek(0)
#         _file = fp.read()
#         post.post_image.put(_file, content_type=image.content_type)
#     post.save()
#     return JSONResponse(status_code=200, 
#                         content={"message": "Post created"})



# class ProductModel(str, Enum):
#     all_products = "all"
#     single_product = 'product_id'
#     subscriptions = 'subscriptions'
#     all_posts = 'all_posts'
#     single_post = 'single_post'
#     all_mongo_products = 'all_mongo_products'

# @router.get("/query_db/{query}/{filter}")
# async def query_db(query: ProductModel, 
#                    filter: Optional[str] = None):

#     if query == ProductModel.single_post:
#         p = Posts.objects.get(id=filter)
#         j = p.to_json()
#         return loads(j)
    
    # if query == ProductModel.all_posts:
    #     lst = []
    #     post = Posts.objects.all()
    #     for a in post:
    #         d = {}            
    #         d['_id'] = str(a['id'])
    #         d['title'] = a.title
    #         d['headline'] = a.headline
    #         d['post_image'] = str(base64.b64encode(a.post_image.read()).decode('utf-8'))
    #         d['content_type'] = a.post_image.content_type
    #         lst.append(d)

    #     return loads(dumps(lst))
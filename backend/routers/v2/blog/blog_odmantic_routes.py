from starlette.responses import JSONResponse
from starlette.requests import Request
from fastapi.responses import RedirectResponse, FileResponse, JSONResponse

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
from orjson import loads, dumps
from enum import Enum
import tempfile
import base64
from pydantic import BaseModel
from typing import List
from fastapi import HTTPException, APIRouter
from odmantic import Model, ObjectId, Field, EmbeddedModel

from ....config.fastapi_users import fastapi_users
from ....config.config import get_settings
from ....utils import Utils
from ....apis.deps import *
from ....db.schemas import User, PostsModel, PydanticModels as pm
from ....db.conn import engine
from ....db.conn import db

router = APIRouter()
settings = get_settings()

# https://pymongo.readthedocs.io/en/stable/api/gridfs/index.html

class Comments(EmbeddedModel):
    comment: str = ''
    
class Posts(Model):
    title: str
    headline: str
    content: str
    # headline_img: Optional[str]
    # post_image: ObjectId
    # comments: Comments = Field(default='')
    
    class Config:# https://art049.github.io/odmantic/modeling/
        collection = "Posts"
        anystr_strip_whitespace: True


# https://art049.github.io/odmantic/usage_fastapi/#getting-all-the-trees
# https://art049.github.io/odmantic/engine/#fetch-multiple-instances
# @router.get("/blog/query_db/{query}/{filter}", response_model=List[Posts])
# async def read_all_posts():
#     print('query_db blog: ')
#     trees = await engine.find(Posts)
#     return trees

'''
@app.get("/", response_description="List all students", response_model=List[StudentModel])
async def list_students():
    students = await db["students"].find().to_list(1000)
    return students
'''
@router.get("/blog/query_db/{query}/{filter}", response_model=List[PostsModel])
async def read_all_posts():
    p = await db["Posts"].find().to_list(1000)
    return p





@router.get("/single_post/{id}", response_model=Posts)
async def read_post_by_id(id: ObjectId):
    tree = await engine.find_one(Posts, Posts.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@router.put("/post_blog_form", response_model=Posts)
async def create_post(post: Posts):
    print(post)
    # await engine.save(tree)
    return post
    # return ''

# @app.post("/post_blog_form", response_description="Add new student", response_model=PostModel)
# async def create_student(student: StudentModel = Body(...)):
#     student = jsonable_encoder(student)
#     new_student = await db["students"].insert_one(student)
#     created_student = await db["students"].find_one({"_id": new_student.inserted_id})
#     return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_student)

# @router.post("/post_blog_form")
# def blog(title: str = Form(...),
#          headline: str = Form(...),
#          image: UploadFile = File(...), 
#          imageList: List[UploadFile] = File(...),
#          content: str = Form(...)):
    
#     print('title: ', title)
#     print('headline: ', headline)
#     print('image: ', image)
#     print('image list: ', {"filenames": [file.filename for file in imageList]})
#     print('content: ', content)
    
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
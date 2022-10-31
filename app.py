from fastapi import FastAPI
from routes.user import user
from docs import tags_metadata


app = FastAPI(
    title='REST API with FastAPI and Mongo DB',
    description= 'This is a basic REST API using FastAPI and MongoDB',
    version='1.0.0',
    openapi_tags=tags_metadata
)

app.include_router(user)

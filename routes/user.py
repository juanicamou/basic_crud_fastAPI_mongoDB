from hashlib import new
from operator import ne
from re import U
from fastapi import APIRouter
from config.db import conn
from schemas.user import userEntity, usersEntity
from models.user import User
from passlib.hash import sha256_crypt

user = APIRouter()

@user.get('/users')
def find_all_user():
    return usersEntity(conn.local.user.find())

@user.post('/users')
def create_user(user: User):
    
    new_user = dict(user)
    new_user['password'] = sha256_crypt.encrypt(new_user['password'])
    del new_user['id']
    
    id = conn.local.user.insert_one(new_user).inserted_id

    user_created = conn.local.user.find_one({'_id': id})

    return userEntity(user_created)
    

@user.get('/users/{id}')
def find_user():
    return 'Hello World'

@user.put('/users/{id}')
def update_user():
    return 'Hello World'

@user.delete('/users/{id}')
def delete_user():
    return 'Hello World'

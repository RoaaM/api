from fastapi import FastAPI
# to make some variable optional
from typing import Optional
from pydantic import BaseModel

# create instance of fastapi
app = FastAPI()

@app.get('/')
# router (html or json in api)
def root():
    return "Hello Worlds"
            


# decorator (in the parantesis the end point)
@app.get('/api/root')

# router (html or json in api)
def root():
    return {"server":"my first api"}
            


@app.get('/api/users')

def users_info():
    return {"username" : "roaa mamoun",
            "age":24,
            "major":"data science"}

# for api testing we use postman or we just type docs insted of endpoint in the url


@app.get('/api/users/id/{id}')
def get_id(id : int, is_active : bool, age:Optional[int] = None):
    return {"user_id":id, "is_active":is_active, "age":age}

# @app.get('/api/users/is_active/{is_active}')
# def active_status(is_active : bool):
    # if is_active: return {"active":is_active}
    # return {"is_active":"not active"}


# define the fields inside the class
# this class will inherts BaseModel
class User(BaseModel):
    id : int
    username : str


# to sent values
# this not parameter this request body
@app.post('/api/users')
def add_new_user(user:User):
    return user           #if we want  just username we type  user.username


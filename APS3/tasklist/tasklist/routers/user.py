# pylint: disable=missing-module-docstring, missing-function-docstring, invalid-name
import uuid

from typing import Dict

from fastapi import APIRouter, HTTPException, Depends

from ..database import DBSession, get_db
from ..models import User

router = APIRouter()



@router.get(
    '',
    summary='Reads user list',
    description='Reads the whole user list.',
    response_model= list,
)
async def read_tasks(db: DBSession = Depends(get_db)):
    return db.read_users()


@router.post(
    '',
    summary='Creates a new user',
    description='Creates a new user and return its user ',
    response_model=User,
)
async def create_user( user : User, db: DBSession = Depends(get_db)):
    return db.create_user(user)


@router.put(
    '/{username}',
    summary='Replaces an user',
    description='Replaces an user identified by its username.',
)
async def replace_task(
        username: str,
        user: User,
        db: DBSession = Depends(get_db),
):
    try:
        db.replace_user(username, user)
    except KeyError as exception:
        raise HTTPException(
            status_code=404,
            detail='Task not found',
        ) from exception


#Qual a diferença entre o patch e o put nesse caso?
@router.patch(
    '/{username}',
    summary='Alters an user',
    description='Alters an user identified by its username.',
)
async def replace_task(
        username: str,
        user: User,
        db: DBSession = Depends(get_db),
):
    try:
        db.replace_user(username, user)
    except KeyError as exception:
        raise HTTPException(
            status_code=404,
            detail='Task not found',
        ) from exception
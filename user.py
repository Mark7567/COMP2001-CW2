from models import user_schema, users_schema, User
from config import db
from flask import make_response, abort
import requests

#Reads all entries - Tested - Works as intended
def read_all():
    user = User.query.all()
    return users_schema.dump(user)


#Create - Tested - Works as intended
def create(user):
    user_id = user.get("user_id")
    existing_user = User.query.filter(User.user_id == user_id).one_or_none()

    if existing_user is None:
        new_user = user_schema.load(user, session=db.session)
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user), 201
    else:
        abort(406, f'User with user ID {user_id} already exists')


#Retrieve one user - Tested - Works as intended
def retrieve(user_id):
    user = User.query.filter(User.user_id == user_id).one_or_none()

    if user is not None:
        return user_schema.dump(user)
    else:
        abort(404, f'User with user ID {user_id} cannot be found')
        

#Delete one user - Tested - Works as intended
def delete(user_id):
    existing_user = User.query.filter(User.user_id == user_id).one_or_none()

    if existing_user:
        db.session.delete(existing_user)
        db.session.commit()
        return make_response(f'{user_id} has been successfully deleted', 200)
    else:
        abort(404, f'User with user ID {user_id} cannot be found')


#Authenticate
def authenticate():
    auth_url = 'https://web.socem.plymouth.ac.uk/COMP2001/auth/api/users'
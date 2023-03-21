from flask_app.env.main2 import app
from flask import request, current_app

with app.test_request_context('/user/'):
    request.path  # получим полный путь к запрашиваемой странице(без домена).
    request.method
    current_app.name

'/products'
'GET'
'main2'
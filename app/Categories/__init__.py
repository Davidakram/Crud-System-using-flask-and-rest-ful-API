from flask import  Blueprint


Categories_blueprint= Blueprint('categories', __name__, url_prefix='/categories')

from app.Categories import views

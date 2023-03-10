from flask import  Blueprint


Products_blueprint= Blueprint('', __name__, url_prefix='/')

from app.Products import  views

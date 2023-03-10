from flask import  Flask
from  app.models import  db
from app.config import  projectConfig as AppConfig   # this dict
from app.models import Products,Categories
from flask_migrate import Migrate
from flask_restful import Api

from app.Products.api.views import AllProducts,ProductUpdate_Delete_OneProduct


def create_app(config_name):
    app = Flask(__name__)
    current_config = AppConfig[config_name]  # class
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config # search in this class about class variable with this name
    app.config['SECRET_KEY'] = current_config.SECRET_KEY

    app.config.from_object(current_config)
    db.init_app(app)
    migrate = Migrate(app, db, render_as_batch=True)



    from app.Categories import Categories_blueprint
    from app.Products import Products_blueprint
  
    app.register_blueprint(Categories_blueprint)
    app.register_blueprint(Products_blueprint)

    api = Api(app)
    api.add_resource(AllProducts, '/api/products')
    api.add_resource(ProductUpdate_Delete_OneProduct, '/api/products/<int:id>')

    return  app

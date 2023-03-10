from flask_restful import Resource, Api, marshal_with, abort
from app.models import Products
from app.Products.api.serializers import ProductsSerializer,CategorySerializer
from  app.Products.api.parser import  product_parser
from app.models import db


class AllProducts(Resource):
    @marshal_with(ProductsSerializer)
    def get(self):
        products=  Products.query.all()
        return products

    @marshal_with(ProductsSerializer)
    def post(self):
        products = product_parser.parse_args() 
        product = Products(**products)
        db.session.add(product)
        db.session.commit()
        return  product, 201
    
class ProductUpdate_Delete_OneProduct(Resource):
    @marshal_with(ProductsSerializer)
    def get(self, id):
        product = Products.query.get(id)
        if product:
            return product, 200

        return abort(404, message="Post not found Please Enter Your valid Id.")

    @marshal_with(ProductsSerializer)
    def put(self, id):
        product = Products.query.get(id)
        if product:
            product_args = product_parser.parse_args()
            product.update_post(product_args)
            return product, 200

        return abort(205, message="Post not found Please Enter Your valid Id.")

    def delete(self, id):
        product = Products.query.get(id)
        if product:
            db.session.delete(product)
            db.session.commit()
            return {"This Post":"Deleted Successfully."}
        return abort(205,'Post not found , please reload the page')
from flask_restful import fields
CategorySerializer= {
    'id': fields.Integer,
    'name': fields.String,
}



ProductsSerializer= {
    'id':fields.Integer,
    'title' :fields.String,
    'body': fields.String,
}
from flask_restful import  reqparse

product_parser = reqparse.RequestParser()

product_parser.add_argument('title', type=str,help='Title is required', required=True )
product_parser.add_argument('body', type=str,help='Body is required' ,required=True )

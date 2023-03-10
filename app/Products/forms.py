from flask_wtf import FlaskForm
from wtforms import StringField,FileField
from wtforms.validators import DataRequired, ValidationError


class ProductForm(FlaskForm):
    title = StringField('Title')
    body = StringField('Body')



class CategoryForm(FlaskForm):
    name = StringField('Category Name')
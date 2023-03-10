from flask import render_template
from app.models import Categories 
from app.Categories import Categories_blueprint


@Categories_blueprint.route('/')
def get_categories():
    categories=Categories.query.all()
    return render_template('Categories.html',categories=categories )

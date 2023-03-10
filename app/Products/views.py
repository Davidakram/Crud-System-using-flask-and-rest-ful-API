from app.models import Products
from flask import Flask,render_template,redirect,request,url_for,send_file
from app.Products import Products_blueprint
from sqlalchemy.sql import func
from app import db
from app.Products.forms import ProductForm
from app.models import Categories




@Products_blueprint.route('/')
def all_Products():
    products=Products.query.all()
    return render_template('Home.html',products=products)


# # # showing details of a particular product
@Products_blueprint.route('/<int:id>')
def one_product(id):
    product=Products.query.get_or_404(id)
    return render_template('one_product.html',product=product)

# #delete a particular product
@Products_blueprint.route('/<int:id>/delete')
def delete(id):
    product=Products.query.get_or_404(id)
    res =product.delete_object()
    if res:
        return redirect(url_for('all_Products'))
    



@Products_blueprint.route('/create', methods = ['POST','GET'],endpoint="addnewproduct")
def addNewProduct():
    products  = ProductForm()
    if request.method == 'GET':
        return render_template("Add.html",form=products,category=Categories.query.all())
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        category = request.form['category']
        new_product=Products(title=title,body=body,category_id=category)
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('all_Products'))
 

# # # editing a particular product
@Products_blueprint.route('/edit/<int:id>/', methods=('GET', 'POST'))
def edit(id):
    product=Products.query.get_or_404(id)
    if request.method == 'GET':
        return render_template('edit.html',form=product,category=Categories.query.all())
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        category = request.form['category']
        product.title=title
        product.body=body
        product.category_id=category
        product.updated_at=func.now()
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('all_Products'))

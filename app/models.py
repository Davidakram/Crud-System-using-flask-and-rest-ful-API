from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()


class Categories(db.Model):
    __tablename__= 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    products = db.relationship('Products', backref='department', lazy=True)

    def __str__(self):
        return f"{self.name}"
    

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body= db.Column(db.String(100),unique=True, nullable=True)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now()) 
    updated_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now()) 
    img = db.Column(db.Text, nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable= True)


    def __str__(self):
        return f"{self.name}"

    def delete_object(self):
        db.session.delete(self)
        db.session.commit()
        return True
    
    def update_post(self, updated_data):
        self.title = updated_data["title"]
        self.body = updated_data["body"]
        db.session.add(self)
        db.session.commit()
        return True
    


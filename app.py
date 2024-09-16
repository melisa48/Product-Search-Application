import os
from flask import Flask, request, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Optional
from sqlalchemy import or_

# Print current working directory
print("Current working directory:", os.getcwd())

# Print absolute path of the templates folder
print("Templates folder:", os.path.abspath(os.path.join(os.getcwd(), 'templates')))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PRODUCTS_PER_PAGE'] = 10

db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)

class SearchForm(FlaskForm):
    query = StringField('Search', validators=[DataRequired()])
    min_price = FloatField('Min Price', validators=[Optional(), NumberRange(min=0)])
    max_price = FloatField('Max Price', validators=[Optional(), NumberRange(min=0)])
    category = StringField('Category')
    submit = SubmitField('Search')

def init_db():
    db.create_all()
    if Product.query.count() == 0:
        print("Initializing database with sample products...")
        products = [
            Product(name='Laptop', price=999.99, category='Electronics'),
            Product(name='Smartphone', price=499.99, category='Electronics'),
            Product(name='Tablet', price=299.99, category='Electronics'),
            Product(name='Desk Chair', price=199.99, category='Furniture'),
            Product(name='Coffee Maker', price=79.99, category='Appliances')
        ]
        db.session.add_all(products)
        db.session.commit()
        print("Database initialized.")

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    print(f"Request method: {request.method}")
    print(f"Form validated: {form.validate_on_submit()}")
    
    if form.validate_on_submit():
        query = form.query.data
        min_price = form.min_price.data if form.min_price.data is not None else None
        max_price = form.max_price.data if form.max_price.data is not None else None
        category = form.category.data

        print(f"Search query: {query}")
        print(f"Min price: {min_price}")
        print(f"Max price: {max_price}")
        print(f"Category: {category}")

        products = Product.query.filter(Product.name.ilike(f'%{query}%'))

        if min_price is not None:
            products = products.filter(Product.price >= min_price)
        if max_price is not None:
            products = products.filter(Product.price <= max_price)
        if category:
            products = products.filter(Product.category.ilike(f'%{category}%'))

        products = products.all()
        
        print(f"Number of products found: {len(products)}")
        for product in products:
            print(f"Found: {product.name} - ${product.price} ({product.category})")

        return render_template('index.html', form=form, products=products)
    else:
        print("Form errors:", form.errors)

    return render_template('index.html', form=form)

@app.route('/check_db')
def check_db():
    products = Product.query.all()
    print(f"Total products in database: {len(products)}")
    for product in products:
        print(f"Product: {product.name} - ${product.price} ({product.category})")
    return render_template('check_db.html', products=products)

if __name__ == '__main__':
    with app.app_context():
        init_db()
    print("Starting Flask development server...")
    app.run(debug=True)
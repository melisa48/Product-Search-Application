# Product Search Application
This is a simple web application built with Flask that allows users to search for products in a database. The application supports searching by product name, filtering by price range, and categorizing products. It uses SQLite as the database and SQLAlchemy as the ORM (Object-Relational Mapping) tool.

## Features

- Search for products by name.
- Filter results based on minimum and maximum price.
- Filter results by product category.
- Displays search results with product name, price, and category.
- Initializes the database with sample products on the first run.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework in Python.
- **SQLAlchemy**: An SQL toolkit and Object-Relational Mapping (ORM) system for Python.
- **Flask-WTF**: An extension for Flask that simplifies form handling.
- **SQLite**: A self-contained, serverless SQL database engine.

## Getting Started

### Prerequisites

Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/product-search-app.git
   cd product-search-app
 2. Install the required packages
     `pip install flask flask-sqlalchemy flask-wtf`
 3. Running the Application
- Make sure you're in the project directory and your virtual environment is activated (if you created one).
- Run the application:
- `python app.py`
4. Open your web browser and go to http://127.0.0.1:5000.

## Database Initialization
- The application will automatically create a SQLite database file named products.db in the project directory if it doesn't already exist. It will also populate the database with sample products on the first run.

## Usage
1. Enter a product name in the search field and click "Search" to find products.
2.  Optionally, specify minimum and maximum prices to filter results.
3.  You can also filter by category if desired.

## Contributing
- Feel free to open issues or submit pull requests if you have suggestions or improvements for this project.

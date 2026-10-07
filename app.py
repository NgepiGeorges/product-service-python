"""Product Service (Python / Flask) for the Algonquin Pet Store.

Rewrite of the original Rust product-service so it can run on
Azure App Service (Python is natively supported; Rust is not).
Same API as before: GET /products returns the product catalog as JSON.
"""
import os

from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_cors import CORS

# Factor III (Config): load settings from a local .env file if it exists.
# Real environment variables (e.g. Azure App Settings) take precedence.
load_dotenv()

app = Flask(__name__)

# Allow the store-front (served from another origin) to call this API.
CORS(app)

PRODUCTS = [
    {"id": 1, "name": "Dog Food", "price": 19.99},
    {"id": 2, "name": "Cat Food", "price": 34.99},
    {"id": 3, "name": "Bird Seeds", "price": 10.99},
]


@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(PRODUCTS)


if __name__ == "__main__":
    # Local run: the port comes from the environment (default 3030).
    # On Azure App Service, gunicorn starts the app instead of this block.
    port = int(os.getenv("PORT", "3030"))
    app.run(host="0.0.0.0", port=port)

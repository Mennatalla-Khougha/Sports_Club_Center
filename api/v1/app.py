#!/usr/bin/python3
"""starts a Flask web application"""
from os import getenv
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from flask_cors import CORS
from website import club

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

@app.teardown_appcontext
def close_db(exception):
    """call the close method"""
    storage.close()

@app.errorhandler(404)
def error_404(error):
    """returns a JSON-formatted 404 status code response"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = getenv('API_HOST', '0.0.0.0')
    port = getenv('API_PORT', 5000)
    app.run(host=host, port=port, threaded=True)

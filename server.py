"""
Main module of the server file
"""
from flask import url_for
import config
import json

connex_app = config.connex_app

# Configuring the endpoints
connex_app.add_api("swagger.yml")

# Basic information of the REST API
basic_data={
    'Name': 'IMDB API',
    'Version': 1.0,
    'documentation route': '/ui'
}

# create a URL route in our application for "/"
@connex_app.route("/")
def home():
    """
    Purpose: This function just responds to route '/'
    Returns: basic informaion of the REST API (Format: JSON)

    """
    return json.dumps(basic_data, indent=4)


if __name__ == "__main__":
    connex_app.run(debug=True)

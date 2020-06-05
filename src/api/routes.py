"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db
from api.utils import generate_sitemap
import random
#from models import Person

api = Blueprint('api', __name__)


@api.route('/card', methods=['GET'])
def get_card():
    suits = ["♣", "♠", "♥", "♦"]
    values = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

    random_suits_position = random.randint(0, 3)
    random_values_position = random.randint(0,12)

    body = {
        "suit": suits[random_suits_position],
        "number": values[random_values_position]
    }

    return jsonify(body), 200
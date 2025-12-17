from flask import Blueprint, render_template

#Creating a blueprint named 'bp'
bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return "<h1>Project 1. Portfolio is Live!!</h1>"
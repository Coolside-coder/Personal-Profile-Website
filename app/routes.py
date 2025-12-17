from flask import Blueprint, render_template

#Creating a blueprint named 'bp'
bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return render_template('index.html')
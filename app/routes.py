from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    # This is our "Database" for now. 
    # It's a list of dictionaries.
    projects = [
        {
            "id": 1,
            "name": "Personal Portfolio",
            "description": "A dynamic resume website built with Flask and Bootstrap.",
            "tech": ["Flask", "Jinja2", "Bootstrap"],
            "image": "portfolio.png" # We will use placeholders for now
        },
        {
            "id": 2,
            "name": "Weather App",
            "description": "Real-time weather fetching using OpenWeatherMap API.",
            "tech": ["Python", "API", "JSON"],
            "image": "weather.png"
        },
        {
            "id": 3,
            "name": "To-Do List",
            "description": "A task manager with database persistence.",
            "tech": ["SQLite", "SQLAlchemy", "Forms"],
            "image": "todo.png"
        }
    ]

    # Pass the 'projects' list to the template
    # The variable name on the left (projects) is what the HTML sees.
    return render_template('index.html', projects=projects)
from flask import Blueprint, render_template, abort

bp = Blueprint('main', __name__)

# ------ DATA SOURCE {MOVED GLOBAL} ---------
# In a real app, this data would come from a database.

PROJECTS = [
    {
        "id": 1,
        "name": "Personal Portfolio",
        "description": "A dynamic resume website built with Flask and Bootstrap.",
        "details": "This project uses Jinja2 inheritance for cleaner code and Bootstrap 5 for responsiveness. It features dynamic routing and a scalable application factory structure.",
        "tech": ["Flask", "Jinja2", "Bootstrap"],
        "repo_link": "https://github.com/yourname/portfolio",
    },
    {
        "id": 2,
        "name": "Weather App",
        "description": "Real-time weather fetching using OpenWeatherMap API.",
        "details": "Users can enter a city name to get the current temperature, humidity, and wind speed. It handles API errors gracefully and caches results for performance.",
        "tech": ["Python", "API", "JSON"],
        "repo_link": "https://github.com/yourname/weather",
    },
    {
        "id": 3,
        "name": "To-Do List",
        "description": "A task manager with database persistence.",
        "details": "A CRUD application allowing users to add, edit, delete, and mark tasks as complete. Uses SQLite for storage and SQLAlchemy ORM for database interactions.",
        "tech": ["SQLite", "SQLAlchemy", "Forms"],
        "repo_link": "https://github.com/yourname/todo",
    }
]


@bp.route('/')
def home():
    return render_template('index.html', projects=PROJECTS)


#New Dynamic Route
@bp.route('/project/<int:id>')
def project_detail(id):
    # 1. Find the project with the matching ID.
    # This is a python list comprehension (a shortcut loop)
    # next() grabs the first match it finds.
    project = next((p for p in PROJECTS if p['id'] == id), None)
    
    # 2. If no project matches that id, return a 404 ERROR
    if project is None:
        abort(404)
    
    # 3. Render the detail template with the specific project data.
    return render_template('project_detail.html', project=project)

# This decorator tells flask to handle 404 errors using this function
# 'app_errorhandler' means it catches errors for the entire application, not just this blueprint.
@bp.app_errorhandler(404)
def not_found_error(error):
    # We return the template AND the status code 404.
    # By default, Flask returns 200 (OK), so we must be explicit here.
    return render_template('404.html'), 404
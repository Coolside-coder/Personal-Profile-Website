from flask import Flask
#TRIAL OF SCENE
def create_app():
    app = Flask(__name__)
    
    # Required for session/flash messages.
    # In production, this should be a complex random string in an .env file.
    app.config['SECRET_KEY'] = 'dev-secret-key-123'
    
    from app import routes
    app.register_blueprint(routes.bp)
    
    return app

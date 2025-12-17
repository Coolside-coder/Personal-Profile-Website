from app import create_app

app = create_app()

if __name__ == '__main__':
    #Debug = True  allows the server to auto-reload when you update changes
    app.run(debug=True)
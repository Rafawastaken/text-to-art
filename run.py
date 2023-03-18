from app import create_app

if __name__ == "__main__":
    with open('creds.txt', 'r') as f:
        api_key = f.read()


    app = create_app(api_key=api_key)
    app.run(debug = True)
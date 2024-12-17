from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Testing out Jenkins CI/CD pipeline! on Windows! Hehe!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
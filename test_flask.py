from flask import Flask

app = Flask(__name__)

@app.route('/')
def test_flask():
    return 'good night!'

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    # return "Hello, World!"
    return "<html><button id='button_id' name='test' onClick='t()'>Test</button></html>"

def t():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:name>')
def hi(name):
    return "Hi " + name + "!"

@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    return word * num

app.run(debug=True)
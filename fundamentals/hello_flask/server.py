from flask import Flask  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/success')
def success():
    return "success"

@app.route('/hello/<placeholder>')
def hello(placeholder):
    return f"hello {placeholder}"

@app.route('/hi/<string:banana>/<int:num>')
def hi(banana, num):
    return f"Hi {banana * num}"

app.run(debug=True)    # Run the app in debug mode.


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('normal_board.html')

@app.route('/4')
def small():
    return render_template('long_board.html')

@app.route('/<int:x>/<int:y>')
def x_y():
    return render_template('x_by_y.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
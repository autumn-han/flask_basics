from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('normal_board.html')

@app.route('/<int:num>')
def small(num):
    if num == 1:
        x1 = 1
        y2 = 0
        z3 = 1
    elif num % 2 == 1:
        x1 = 1
        y2 = 0
        z3 = num + 1
    else:
        x1 = 1
        y2 = 1
        z3 = num - 1
    return render_template('num_board.html', x=x1, y=y2, z=z3)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
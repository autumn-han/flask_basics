from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('normal_board.html', x=4, y=4, z=4)

@app.route('/<int:num>')
def small(num, x1, y2, z3):
    if num == 1:
        x1 = 1
        y2 = 0
        z3 = 0
    elif num % 2 == 1:
        x1 = 1
        y2 = 0
        z3 = num + 1
    else:
        x1 = 1
        y2 = 1
        z3 = num
    return render_template('normal_board.html', x=x1, y=y2, z=z3)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
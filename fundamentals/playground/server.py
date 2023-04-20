from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/play')
def play():
    return render_template('play.html')

@app.route('/<int:num>')
def xrepeat(num):
    return render_template(xrepeat.html, times=num)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
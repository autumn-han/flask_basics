from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/play')
def play():
    return render_template('play.html')

@app.route('/play/<int:num>')
def xrepeat(num):
    return render_template('xrepeat.html', times=num)

@app.route('/play/<int:num>/<color>')
def box_color(num, color):
    return render_template('box_color.html', times=num, box_color=color)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
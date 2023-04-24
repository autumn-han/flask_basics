from flask import Flask, render_template, redirect, session

app = Flask(__name__)

app.secret_key = 'three days without showering'

@app.route('/')
def home():
    if 'num' not in session:
        session['num'] = 0
    else:
        session['num'] += 1
    return render_template('index.html')

@app.route('/destroy_session')
def clear():
    session.clear()
    return redirect('/')

@app.route('/by_two')
def increment_by_two():
    if 'num' not in session:
        session['num'] = 0
    else:
        session['num'] += 2
    return render_template('index.html')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if (__name__) == '__main__':
    app.run(debug=True, port=5001)
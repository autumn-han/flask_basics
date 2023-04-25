from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    session['fname'] = request.form['fname']
    session['lname'] = request.form['lname']
    session['email'] = request.form['email']
    session['comment'] = request.form['comment']
    return redirect('/')

@app.route('/display_info')
def display():
    return render_template('display_info')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
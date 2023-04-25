from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = 'bobby is cute'

@app.route('/')
def home():
    print("hello")
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    print(request.form)
    session['fname'] = request.form['fname']
    session['lname'] = request.form['lname']
    session['email'] = request.form['email']
    session['comment'] = request.form['comment']
    return redirect('/display_info')

@app.route('/display_info')
def display():
    return render_template('display_info.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
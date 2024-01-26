from flask import Flask, render_template, request, redirect, url_for, session
import json
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Routes
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None  # Initialize error variable

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        with open('users.json', 'r') as file:
            users = json.load(file)

        if username in users and check_password_hash(users[username]['password'], password):
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            error = 'Invalid username or password'  # Set error message

    return render_template('login.html', error=error)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password == confirm_password:
            hashed_password = generate_password_hash(password)

            with open('users.json', 'r') as file:
                users = json.load(file)

            users[username] = {'password': hashed_password}

            with open('users.json', 'w') as file:
                json.dump(users, file)

            return render_template('signup_success.html', username=username)

        else:
            return render_template('signup.html', error='Passwords do not match')

    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html', username=session['username'])
    else:
        return redirect(url_for('login'))

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


# Run the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

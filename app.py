from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  
database = []

class User:
    def __init__(self, name, phone, password):
        self.name = name
        self.phone = phone
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


def register_user(name, phone, password):
    for user in database:
        if user.phone == phone:
            return "Phone number already registered"
    new_user = User(name, phone, password)
    database.append(new_user)
    return "Registration successful"

def login_user(phone, password):
    for user in database:
        if user.phone == phone and user.verify_password(password):
            return f"Welcome back, {user.name}!"
    return "Invalid login credentials"

def unregister_user(phone):
    for i, user in enumerate(database):
        if user.phone == phone:
            del database[i]
            return f"User with phone {phone} unregistered"
    return "User not found"


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        password = request.form['password']
        message = register_user(name, phone, password)
        return render_template('register.html', message=message)
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        phone = request.form['phone']
        password = request.form['password']
        message = login_user(phone, password)
        return render_template('login.html', message=message)
    return render_template('login.html')

@app.route('/unregister', methods=['GET', 'POST'])
def unregister():
    if request.method == 'POST':
        phone = request.form['phone']
        message = unregister_user(phone)
        return render_template('unregister.html', message=message)
    return render_template('unregister.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from config import Config
from models import init_db, mysql
from forms import LoginForm, RegisterForm

app = Flask(__name__)
app.config.from_object(Config)
init_db(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@app.route('/')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM students WHERE email=%s", (email,))
        user = cur.fetchone()
        if user and user[5] == password:  # Check if password matches
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Login Unsuccessful. Please check username and password.', 'danger')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        nshe_number = form.nshe_number.data
        email = form.email.data
        password = form.password.data
        role = 'student'
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO students (first_name, last_name, nshe_number, email, password, role) VALUES (%s, %s, %s, %s, %s, %s)",
                    (first_name, last_name, nshe_number, email, password, role))
        mysql.connection.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@login_manager.user_loader
def load_user(user_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM students WHERE id=%s", (user_id,))
    user = cur.fetchone()
    return User(user[0], user[1])  # Adjust this based on your user model

if __name__ == '__main__':
    app.run(debug=True)

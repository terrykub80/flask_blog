from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import SignUpForm, LogInForm
from app.models import User

@app.route('/')
def index():
    fruits = ['apple', 'banana', 'orange', 'strawberry', 'watermelon', 'mango', 'blueberry']
    return render_template('index.html', name='Terry', fruits=fruits)
    


@app.route('/posts')
def posts():
    return render_template('posts.html')


@app.route('/signup', methods=["GET", "POST"])
def signup():
    # Create an instance of the SignUpForm
    form = SignUpForm()
    # Check if a POST request AND data is valid
    if form.validate_on_submit():
        print('Form Submitted and Validated')
        # Get data from the form
        email = form.email.data
        username = form.username.data
        password = form.password.data
        print(email, username, password)
        # Check to see if there is a user with username and/or email
        check_user = User.query.filter( (User.username == username) | (User.email == email) ).first()
        if check_user:
            flash(f"The username {username} already exists. Please try again.", 'danger')
            return redirect(url_for('signup'))
        # If check_user is empty, create a new user with form data
        new_user = User(email=email, username=username, password=password)
        # Flash a success message
        flash(f'Thank you {new_user.username} for signing up!', 'success')
        # Redirect back to Home
        return redirect(url_for('index'))

    return render_template('signup.html', form=form)


@app.route('/login')
def login():
    form = LogInForm()

    if form.validate_on_submit():
        print('Form Submitted and Validated')
        username = form.username.data
        password = form.password.data
    return render_template('login.html', form=form)
    
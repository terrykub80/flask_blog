from app import app
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.forms import SignUpForm, LogInForm, PostForm
from app.models import User, Post

@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)
    

@app.route('/posts')
def posts():
    posts = Post.query.all()
    return render_template('posts.html', posts=posts)


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LogInForm()

    if form.validate_on_submit():
        # Get username and password from the form
        username = form.username.data
        password = form.password.data
        print(username, password)
        # Query the user table to see if user exists
        user = User.query.filter_by(username = username).first()
        # Check if user and that password is correct
        if user is not None and user.check_password(password):
            # Log the user in
            login_user(user)
            flash(f"Welcome back {user.username}! You are now logged in!", "success")
            return redirect(url_for('index'))
        else:
            flash("Incorrect username and/or password", "danger")
            redirect(url_for('login'))
        
    # verify_user = User.query.filter( (User.username == username) | (User.password == password) ).all()
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    flash("You have been logged out", "warning")
    return redirect(url_for('index'))



@app.route('/create-post', methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        print(title, body, current_user)
        # Create new post instance and add to db
        new_post = Post(title=title, body=body, user_id=current_user.id)
        flash(f"{new_post.title} has been created!", "success")
        return redirect(url_for('index'))
                
    return render_template('create.html', form=form)
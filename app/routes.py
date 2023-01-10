from app import app
from flask import render_template, redirect, url_for
from app.forms import SignUpForm

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
        # TODO Check to see if there is a user with username and/or email
        # TODO Create a new user with form data

        # Redirect back to Home
        return redirect(url_for('index'))

    return render_template('signup.html', form=form)


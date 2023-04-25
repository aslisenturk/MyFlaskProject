# Import necessary modules from the Flask library
from flask import Flask, render_template, session, request, redirect, url_for, abort

# Create an instance of the Flask class
app = Flask(__name__)
# Secret key for the app which is needed for session management
app.secret_key = b"!6483hsf_"


# Function to get the current username and whether a user is logged in or not
def get_current_username():
    username = ""
    login_auth = False
    if 'username' in session:
        username = session['username']
        login_auth = True
    return username, login_auth


# Route to the home page ("/")
@app.route("/")
def index():
    username, login_auth = get_current_username()
    return render_template("index.html", username=username, login_auth=login_auth)


# Route to the about page ("/about")
@app.route("/about")
def about():
    username, login_auth = get_current_username()
    # Render the about.html template and pass the username and login_auth variables to the template
    return render_template("about.html", username=username, login_auth=login_auth)


# Route to the contact page ("/contact")
@app.route("/contact")
def contact():
    username, login_auth = get_current_username()
    # Render the contact.html template and pass the username and login_auth variables to the template
    return render_template("contact.html", username=username, login_auth=login_auth)


# Route to the blog page ("/blog")
@app.route("/blog")
def blog():
    username, login_auth = get_current_username()
    # Render the blog.html template and pass the username and login_auth variables to the template
    return render_template("blog.html", username=username, login_auth=login_auth)


# Route to handle login requests
@app.route("/login", methods=['GET', 'POST'])
# If there is a POST request, then if the form is submitted with username and password
# Gets the username and password and if these data match the hardcoded values,
# sets the username value in session to that given value
# Then redirects to home page, if the data do not match redirects to login page
# If the form data is missing the username or password, abort the request with a 400 error
def login():
    if request.method == 'POST':
        if request.form:
            if 'username' in request.form and 'password' in request.form:
                username = request.form['username']
                password = request.form['password']
                if username == 'admin' and password == 'admin':
                    session['username'] = username
                    return redirect(url_for('index'))
                else:
                    return redirect(url_for('login'))
        abort(400)
    # If there is not a POST request, render the login.html template
    # and pass the username and login_auth variables to the template
    username, login_auth = get_current_username()
    return render_template("login.html", username=username, login_auth=login_auth)

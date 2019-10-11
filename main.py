from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('form.html', username = '', username_error = '', password= '', password_error = '', verify='', verify_error='',email='',email_error='')
   
@app.route('/error', methods=['POST'])
def validation():
    
    username = request.form['username']
    password = request.form['password']
    verify= request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    # username_error
    if len(username) < 3 or len(username) > 20 or " " in username:
        username_error = "This is not a valid username"
    # password_error
    if len(password) < 3 or len(password) > 20 or " " in password:
        password_error = "This is not a valid password"
    # verify_error
    if not verify == password:
        verify_error = "The verification of the password does NOT match"
    # email_error
    if not email == '':
        if not 3 < len(email) < 20 or " " in email or email.count("@") > 1 or email.count(".") > 1:
            email_error = "Format the email properly"
 
    # combining all errors
    if not username_error and not password_error and not verify_error and not email_error:
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('form.html', username=username, username_error=username_error, password_error = password_error, verify_error=verify_error, email=email, email_error=email_error)

@app.route('/welcome')
def valid_signup():
    username = request.args.get('username')
    return render_template('welcome_form.html', username=username)

app.run()
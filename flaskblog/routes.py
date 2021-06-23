from flask import render_template, url_for , flash , redirect
from flaskblog.forms import RegistrationForm , LoginForm
from flaskblog import app,db,bcrypt
from flaskblog.models import User, Post

posts=[ 
        {
        'author':'Anurag Shukla',
        'title' : 'Post name 1',
        'content' : 'First post content',
        'date_posted' : 'June 15 2021'
        },
        {
        'author':'Sameer Ahmed',
        'title' : 'Post name 2',
        'content' : 'Second post content',
        'date_posted' : 'June 17 2021'
        }
      ]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)


@app.route("/about")
def about():
    return render_template('about.html',title='About')

@app.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created , you can now login !','success')
        return redirect(url_for('login'))

    return render_template('register.html',title='Register', form=form)




@app.route("/login" ,methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('Logged in successfully !', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Failed. Check Email and Password again !','danger')    
    return render_template('login.html',title='Login', form=form)

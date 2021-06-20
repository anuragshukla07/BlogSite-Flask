from flask import Flask , render_template, url_for , flash , redirect
from forms import RegistrationForm , LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '00caf1ee75cf656a5e24c2c36fc57d80'

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
        flash(f'account created for { form.username.data }!','success')
        return redirect(url_for('home'))

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

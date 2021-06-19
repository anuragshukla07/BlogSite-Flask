from flask import Flask , render_template, url_for
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
    return render_template('register.html',title='Register', form=form)



@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html',title='Login', form=form)

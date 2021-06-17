from flask import Flask , render_template, url_for

app = Flask(__name__)

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

@app.route("/login")
def login():
    return render_template('login.html')

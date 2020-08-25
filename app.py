from flask import Flask,render_template,redirect,request,url_for,flash
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SECRET_KEY'] = 'dev'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.Text)

@app.route('/home',methods=['GET','POST'])
def index():
    if request.method=='POST':
        title=request.form.get('title')
        body=request.form.get('body')
        post = Post(title=title, body=body)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!')
        return redirect('display')
    return render_template('index.html')

@app.route('/display')
def display():
    posts=Post.query.all()
    return render_template('display.html',posts=posts)
 


if __name__=='__main__':
    app.run(debug=True)

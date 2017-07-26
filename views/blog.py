from flask import request, render_template, session
from flask_sqlalchemy import SQLAlchemy
from app import app, db
from models import User, Blog

def get_blogData_all():
    # blog = Blog.query.all()
    # user = User.query.all()
    return db.engine.execute('''SELECT User.id AS id, User.username AS username, Blog.id as blog_id, Blog.title as title, Blog.body as body
                                FROM Blog
                                LEFT JOIN User ON user.id = blog.owner_id''')

def checkSession():
    if session:
        return 'True'
    else:
        return 'False'

@app.route('/blog', methods=['GET'])
def blog():

    # if there is no blogs in db, render blank blog
    if not blog:
        return render_template('blog.html')

    else:
        blogID = request.args.get('id') # extract the value of id
        userID = request.args.get('user')

        if userID:
            blogData = Blog.query.filter_by(owner_id=userID).all()
            oneUser = User.query.filter_by(id=userID).first()

            return render_template('singleUser.html',
                                    blogData=blogData,
                                    oneUser=oneUser,
                                    sessionCheck=checkSession())

        if blogID == None: # if value of id returns None render template blog.html


            return render_template('blog.html',
                                    blogList=get_blogData_all(),
                                    sessionCheck=checkSession())
        else:
            oneBlog = Blog.query.filter_by(id=blogID).first()
            oneUser = User.query.filter_by(id=oneBlog.owner_id).first()

            return render_template('singleBlog.html',
                                    oneBlog=oneBlog,
                                    oneUser=oneUser,
                                    sessionCheck=checkSession())

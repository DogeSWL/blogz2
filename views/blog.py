from flask import request, render_template, session
from flask_sqlalchemy import SQLAlchemy
from app import app, db
from models import Users, Blogs

def get_blogData_all():
    return db.engine.execute('''SELECT Users.id AS id, Users.username AS username, Blogs.id as blog_id, Blogs.title as title, Blogs.body as body
                                FROM Blogs
                                LEFT JOIN Users ON Users.id = Blogs.owner_id''')

def checkSession():
    if session:
        return 'True'
    else:
        return 'False'

@app.route('/blog', methods=['GET'])
def blog():
    blog = Blogs.query.all()
        # user = User.query.all()

    # if there is no blogs in db, render blank blog
    if not blog:
        return render_template('blog.html')

    else:
        blogID = request.args.get('id') # extract the value of id
        userID = request.args.get('user')

        if userID:
            blogData = Blogs.query.filter_by(owner_id=userID).all()
            oneUser = Users.query.filter_by(id=userID).first()

            return render_template('singleUser.html',
                                    blogData=blogData,
                                    oneUser=oneUser,
                                    sessionCheck=checkSession())

        if blogID == None: # if value of id returns None render template blog.html


            return render_template('blog.html',
                                    blogList=get_blogData_all(),
                                    sessionCheck=checkSession())
        else:
            oneBlog = Blogs.query.filter_by(id=blogID).first()
            oneUser = Users.query.filter_by(id=oneBlog.owner_id).first()

            return render_template('singleBlog.html',
                                    oneBlog=oneBlog,
                                    oneUser=oneUser,
                                    sessionCheck=checkSession())

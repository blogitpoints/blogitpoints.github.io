from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flaskblog.models import Post, User
from flask_login import current_user, login_required

main = Blueprint('main', __name__)




@main.route("/layout")
def layout():
    users = User.query.all()
    posts = Post.query.all()
    user = current_user
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template("layout.html", posts=posts, title='Home', users=users, image_file=image_file, user=user)


@main.route("/")
@main.route("/home")
def home():
    users = User.query.all()
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template("home.html", posts=posts, title='Home', users=users)


@main.route("/about")
@login_required
def about():
    users = User.query.all()
    posts = Post.query.all()
    return render_template("about.html", posts=posts, title='About Us', users=users)


@main.route("/versions")
@login_required
def versions():
    users = User.query.all()
    posts = Post.query.all()
    return render_template("versions.html", posts=posts, title='Versions', users=users)


@main.route("/trending")
@login_required
def trending():
    users = User.query.all()
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template("trending.html", title='Trending', posts=posts, users=users, image_file=image_file)
import os

from flask import Flask, render_template, redirect, url_for, g
import click
from flask.cli import with_appcontext

from .commands import test

from app.routes.auth import login_required
from app.extensions import db
# from flask_login import current_user


def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY")

    from app.routes import auth
    app.register_blueprint(auth.bp)

    from app.routes import points
    app.register_blueprint(points.bp)
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    # There is no need for a homepage.
    def index():
        return redirect(url_for('auth.login'))

    @app.route('/home')
    def home():
        return render_template('home.html')

    @app.route('/dashboard')
    @login_required
    def dashboard():
        user = db.child('users').child(g.user['localId']).get().val()               #fetch user information from database
        userPoints = db.child('points').child(g.user['localId']).get().val()        #fetch user points from database
        return render_template('dashboard.html', user = user, points = userPoints)  #load the dashboard with the user information

    @app.route('/points')
    @login_required
    def points():
        userPoints = userPoints = db.child('points').child(g.user['localId']).get().val()
        return render_template('points.html', points = userPoints)

    @app.route('/meetteam')
    def meet_team():
        return 'MeetTeam'

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('/error/404.html', title='404'), 404

    return app

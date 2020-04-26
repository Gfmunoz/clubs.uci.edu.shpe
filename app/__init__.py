import os

from flask import Flask, render_template, redirect, url_for
from app.routes.auth import login_required


def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY")

    from app.routes import auth, settings
    from app.routes.search import get_all_users

    # Register routes
    app.register_blueprint(auth.bp)
    app.register_blueprint(settings.bp)

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
        return render_template('dashboard.html')

    @app.route('/team')
    def team():
        return render_template('/team.html')

    @app.route('/search')
    def search():
        users = get_all_users()
        # for user in users:
        #     user.print()
        return render_template('search.html', users=users)

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('/error/404.html', title='404'), 404

    return app

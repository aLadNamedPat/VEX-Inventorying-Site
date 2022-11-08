from flask import Blueprint, render_template
from flask_login import login_required, current_user
from functools import wraps
from . import db, login_manager


def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated:
                return login_manager.unauthorized()
            if ((current_user.urole != role) and (role != "ANY")):
                return login_manager.unauthorized()
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper


main = Blueprint('main', __name__)


@main.route('/')
@main.route('/about')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required(role="coach")
def profile():
    return render_template('profile.html')
    # return render_template('profile.html', name=current_user.name)


@main.route('/inventory')
@login_required(role="ANY")
def Inventory():
    return render_template("inventory.html")

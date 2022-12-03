from flask import Blueprint, render_template, redirect, request, flash, url_for
from flask_login import login_required, current_user, logout_user
from functools import wraps
from .models import User
from . import db, login_manager
dataVal = [
        {
            "name" : "VRC Spin Up Full Field Element & Game Element Kit",
            "price" : 549,
            "count" : 1,
            "SKU" : "276-7500",
            "link" : "https://www.vexrobotics.com/276-7500.html",
            "image" : "https://www.vexrobotics.com/media/catalog/product/cache/d64bdfbef0647162ce6500508a887a85/2/7/276-7500.png"
        },
        {
            "name" : "V5 Robot Battery Li-Ion 1100mAh",
            "price" : 69.99,
            "count" : 1,
            "SKU" : "276-4811",
            "link" : "https://www.vexrobotics.com/276-4811.html",
            "image" : "https://www.vexrobotics.com/media/catalog/product/cache/d64bdfbef0647162ce6500508a887a85/2/7/276-4811-000-v5-robot-battery_1.jpg"

        },
        {
            "name" : "Vision Sensor",
            "price" : 79.99,
            "count" : 1,
            "SKU" : "276-4850",
            "link" : "https://www.vexrobotics.com/276-4850.html",
            "image" : "https://www.vexrobotics.com/media/catalog/product/cache/d64bdfbef0647162ce6500508a887a85/2/7/276-4850-vision-sensor-front.jpg"

        },
        {
            "name" : "Inertial Sensor",
            "price" : 49.99,
            "count" : 1,
            "SKU" : "276-4855",
            "link" : "https://www.vexrobotics.com/276-4855.html",
            "image" : "https://www.vexrobotics.com/media/catalog/product/cache/d64bdfbef0647162ce6500508a887a85/e/3/e33a8364_1.jpg"
        },
        {
            "name" : "Distance Sensor",
            "price" : 45.99,
            "count" : 1,
            "SKU" : "276-4852",
            "link" : "https://www.vexrobotics.com/276-4852.html",
            "image" : "https://www.vexrobotics.com/media/catalog/product/cache/d64bdfbef0647162ce6500508a887a85/2/7/276-4852-_2_.jpg"
        },
        {
            "name" : "Optical Sensor",
            "price" : 45.99,
            "count" : 1,
            "SKU" : "276-7043",
            "link" : "https://www.vexrobotics.com/276-7043.html",
            "image" : "https://www.vexrobotics.com/media/catalog/product/cache/d64bdfbef0647162ce6500508a887a85/2/7/276-7043.jpg"
        },
        {
            "name" : "V5 Robot Brain",
            "price" : 349,
            "count" : 1,
            "SKU" : "276-4810",
            "link" : "https://www.vexrobotics.com/276-4810.html",
            "image" : "https://www.vexrobotics.com/media/catalog/product/cache/d64bdfbef0647162ce6500508a887a85/2/7/276-4810-v5-robot-brain_home_1.jpg"
        },
        {
            "name" : "Rotation Sensor",
            "price" : 39.99,
            "count" : 1,
            "SKU" : "276-6050",
            "link" : "https://www.vexrobotics.com/276-6050.html",
            "image" : "https://www.vexrobotics.com/media/catalog/product/cache/d64bdfbef0647162ce6500508a887a85/2/7/276-6050-_7_.jpg"
        },
        {
            "name" : "V5 Controller",
            "price" : 124.99,
            "count" : 1,
            "SKU" : "276-4820",
            "link" : "https://www.vexrobotics.com/276-4820.html",
            "image" : "https://www.vexrobotics.com/media/catalog/product/cache/d64bdfbef0647162ce6500508a887a85/2/7/276-4820-v5-controller_home.jpg"
        },
        {
            "name" : "V5 Controller",
            "price" : 43.99,
            "count" : 1,
            "SKU" : "276-4831",
            "link" : "https://www.vexrobotics.com/276-4831.html",
            "image" : "https://www.vexrobotics.com/media/catalog/product/cache/d64bdfbef0647162ce6500508a887a85/2/7/276-4831-100-v5-robot-radio-top_1.jpg"
        },
        {
            "name" : "Potentiometer V2",
            "price" : 14.49,
            "count" : 2,
            "SKU" : "276-7417",
            "link" : "https://www.vexrobotics.com/276-7417.html",
            "image" : "https://www.vexrobotics.com/media/catalog/product/cache/d64bdfbef0647162ce6500508a887a85/v/e/vex_v5_potentiometer_back_right_v01_05252021.jpg"
        },
        {
            "name" : "3-Wire Expander",
            "price" : 39.99,
            "count" : 1,
            "SKU" : "276-5299",
            "link" : "https://www.vexrobotics.com/276-5299.html",
            "image" : "https://www.vexrobotics.com/media/catalog/product/cache/d64bdfbef0647162ce6500508a887a85/2/7/276-5299-_2_.jpg"
        },
        {
            "name" : "V5 GPS Sensor",
            "price" : 199.99,
            "count" : 1,
            "SKU" : "276-7405",
            "link" : "https://www.vexrobotics.com/276-7405.html",
            "image" : "https://www.vexrobotics.com/media/catalog/product/cache/d64bdfbef0647162ce6500508a887a85/e/3/e33a7511.jpg"
        },
        {
            "name" : "Bumper Switch 6N",
            "price" : 14.49,
            "count" : 2,
            "SKU" : "276-8010",
            "link" : "https://www.vexrobotics.com/276-8010.html",
            "image" : "https://www.vexrobotics.com/media/catalog/product/cache/d64bdfbef0647162ce6500508a887a85/2/7/276-8010.jpg"
        },
        {
            "name" : "VRC Spin Up Game Element Kit",
            "price" : 149.99,
            "count" : 60,
            "SKU" : "276-7501",
            "link" : "https://www.vexrobotics.com/276-7501.html",
            "image" : "https://www.vexrobotics.com/media/catalog/product/cache/d64bdfbef0647162ce6500508a887a85/2/7/276-7501.jpg"
        },
        {
            "name" : "8T Sprocket, 6P",
            "price" : 19.99,
            "count" : 8,
            "SKU" : "276-8030",
            "link" : "https://www.vexrobotics.com/6p-sprockets.html",
            "image" : "https://www.vexrobotics.com/media/catalog/product/cache/fa9a1d324ff277b0a3724afc40c455f6/2/7/276-8030_1.jpg"
        },
        {
            "name" : "16T Sprocket, 6P",
            "price" : 24.99,
            "count" : 8,
            "SKU" : "276-8328",
            "link" : "https://www.vexrobotics.com/6p-sprockets.html",
            "image" : "https://www.vexrobotics.com/media/catalog/product/cache/fa9a1d324ff277b0a3724afc40c455f6/2/7/276-8328.jpg"           
        },
        {
            "name" : "24T Sprocket, 6P",
            "price" : 24.99,
            "count" : 8,
            "SKU" : "276-8329",
            "link" : "https://www.vexrobotics.com/6p-sprockets.html",
            "image" : "https://www.vexrobotics.com/media/catalog/product/cache/fa9a1d324ff277b0a3724afc40c455f6/2/7/276-8329.jpg"
        },
        {
            "name" : "32T Sprocket, 6P",
            "price" : 24.99,
            "count" : 8,
            "SKU" : "276-8330",
            "link" : "https://www.vexrobotics.com/6p-sprockets.html",
            "image" : "https://www.vexrobotics.com/media/catalog/product/cache/fa9a1d324ff277b0a3724afc40c455f6/2/7/276-8330.jpg"
        },
        {
            "name" : "40T Sprocket, 6P",
            "price" : 24.99,
            "count" : 8,
            "SKU" : "276-8331",
            "link" : "https://www.vexrobotics.com/6p-sprockets.html",
            "image" : "https://www.vexrobotics.com/media/catalog/product/cache/fa9a1d324ff277b0a3724afc40c455f6/2/7/276-8331.jpg"
        },
        {
            "name" : "Chain",
            "price" : 19.99,
            "count" : 200,
            "SKU" : "228-4983",
            "link" : "https://www.vexrobotics.com/6p-sprockets.html",
            "image" : "https://www.vexrobotics.com/media/catalog/product/cache/fa9a1d324ff277b0a3724afc40c455f6/2/2/228-4983_1.jpg"
        }
]


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
def about():
    return render_template('index.html')


# @main.route('/profile')
# @login_required(role="coach")
# def profile():
#     # return render_template('profile.html')
#     return render_template('profile.html', name=current_user.name)


@main.route('/wishlist')
@login_required(role="ANY")
def wishlist():
    return render_template("wishlist.html", data=dataVal)

@main.route('/items')
@login_required(role="ANY")
def items():
    return render_template("all_Items.html", data=dataVal)

@main.route('/profile')
@login_required(role="student")
def profile():
    return render_template("profile.html", team_mates = current_user.team_mates, name = current_user.name)
    
@main.route('/profile', methods=['POST'])
@login_required(role="student")
def profile_post():
    email = request.form.get('CoachEmailRequest')
    user = User.query.filter_by(savedEmail=email).first()
    # print(user)
    # for user in User.query.all():
    #     print(user.name)
    #     print(user.savedEmail)

    if not user or user.urole != "coach":
        flash('Please make sure this is a coach email!')
        return redirect(url_for("main.profile"))
    else:
        if current_user.savedEmail in user.received_requests:
            flash('Request already sent. Please wait for a response')
            return redirect(url_for("main.profile"))
        else:
            user.received_requests[current_user.savedEmail] = current_user.savedEmail
            current_user.received_requests[user.savedEmail] = False
            print(user.received_requests)
            print(current_user.received_requests)
            db.session.add(current_user)
            db.session.add(user)
            db.session.commit()
            print(user.name)
            print(user)
            print(user.received_requests)
            print(current_user)
            print(current_user.received_requests)
            print("5")
            assert user.received_requests[current_user.savedEmail] == current_user.savedEmail
            flash('Request sent successfully, please wait for a response.')
            return redirect(url_for("main.profile"))

@main.route('/teams')
@login_required(role="coach")
def teams():
    savedTeams = []
    for memberEmail in current_user.received_requests.keys():
        savedTeams.append(User.query.filter_by(savedEmail = memberEmail).first())
        print(memberEmail)
        print(User.query.filter_by(savedEmail = memberEmail))
    return render_template("teams.html", unresponded_requests = savedTeams, accepted = current_user.teams)

@main.route('/teams', methods=['POST'])
@login_required(role="coach")
def teams_post():
    pass
from flask import Blueprint, render_template, redirect, request, flash, url_for
from flask_login import login_required, current_user, logout_user
from functools import wraps
from .models import User
from . import db, login_manager
from .forms import WLManageForm, InvModifyForm
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
            user.received_requests[current_user.savedEmail] = False
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
            assert user.received_requests[current_user.savedEmail] == False
            flash('Request sent successfully, please wait for a response.')
            return redirect(url_for("main.profile"))

@main.route('/teams')
@login_required(role="coach")
def teams():
    current_requests = []
    fufilled_requests = []
    for memberEmail in current_user.received_requests.keys():
        if not current_user.received_requests.get(memberEmail):
            current_requests.append(User.query.filter_by(savedEmail = memberEmail).first())
        else:
            fufilled_requests.append(User.query.filter_by(savedEmail = memberEmail).first())
        # print(memberEmail)
        # print(User.query.filter_by(savedEmail = memberEmail))
    return render_template("teams.html", name = current_user.name, unresponded_requests = current_requests, accepted = fufilled_requests)

@main.route('/teams', methods=['POST'])
@login_required(role="coach")
def teams_Post():
    current_requests = []
    fufilled_requests = []
    print(list(request.form.keys())[0])
    if "Add Team" == request.form[list(request.form.keys())[0]]:
        current_user.received_requests[list(request.form.keys())[0][:-1]] = True
        user = User.query.filter_by(savedEmail=list(request.form.keys())[0][:-1]).first()
        user.received_requests[current_user.savedEmail] = True
        user.confirmedRequests = True
        
    if "Reject Team" == request.form[list(request.form.keys())[0]]:
        current_user.received_requests.pop(list(request.form.keys())[0][:-1])
        user = User.query.filter_by(savedEmail=list(request.form.keys())[0][:-1]).first()
        user.received_requests.pop(current_user.savedEmail)
    
    if "Remove Team" == request.form[list(request.form.keys())[0]]:
        current_user.received_requests.pop(list(request.form.keys())[0][:-1])
        user = User.query.filter_by(savedEmail=list(request.form.keys())[0][:-1]).first()
        user.received_requests.pop(current_user.savedEmail)
        user.confirmedRequests = False

    db.session.add(current_user)
    db.session.add(user)
    db.session.commit()
    
    for memberEmail in current_user.received_requests.keys():
        if not current_user.received_requests.get(memberEmail):
            current_requests.append(User.query.filter_by(savedEmail = memberEmail).first())
        else:
            fufilled_requests.append(User.query.filter_by(savedEmail = memberEmail).first())
        # print(memberEmail)
        # print(User.query.filter_by(savedEmail = memberEmail))
    return render_template("teams.html", name = current_user.name, unresponded_requests = current_requests, accepted = fufilled_requests)

@main.route('/inventory')
@login_required(role="ANY")
def inventory():
    modify_form = InvModifyForm()
    invItems = []
    if (current_user.urole == "coach"):
        for name in current_user.inventory.keys():
            invItems.append(current_user.inventory[name])

    elif (current_user.urole == "student" and current_user.confirmedRequests):
        for coachEmail in current_user.received_requests.keys():
            if current_user.received_requests[coachEmail]:
                user = User.query.filter_by(savedEmail=coachEmail).first()
                for name in user.inventory.keys():
                    invItems.append(user.inventory[name])
    return render_template("inventory.html", all_items = dataVal, inventory = invItems, modify_form=modify_form)

@main.route('/inventory', methods=['POST'])
@login_required(role="ANY")
def inventory_post():
    invItems = []
    itemName = request.form.get('selectItemName')
    itemNumber = int(request.form.get('amountInserted'))
    count = 0
    for item in dataVal:
        if item["name"] and item["name"] == itemName:
            itemSKU = item["SKU"]
        if item["SKU"] == itemName:
            itemSKU = itemName
            itemName = item["name"]
    if (current_user.urole == "coach"):
        if itemName in current_user.inventory:
            count = current_user.inventory[itemName]["Count"]
        count += itemNumber
        current_user.inventory[itemName] = {
            "Name": itemName,
            "SKU" : itemSKU,
            "Count" : count,
            "AvailCount": count
        }
        for name in current_user.inventory.keys():
            invItems.append(current_user.inventory[name])

    elif (current_user.urole == "student" and current_user.confirmedRequests):
        coachEmail = ""
        for email in current_user.received_requests.keys():
            if email != current_user.email:
                coachEmail = email
        user = User.query.filter_by(email=coachEmail).first()
        #if itemName in user.inventory:
        count = user.inventory[itemName]["Count"]
        availCount = count
        if user.inventory[itemName].get("AvailCount"):
            availCount = user.inventory[itemName]["AvailCount"]
        if itemNumber > int(availCount):
            flash(f"Not enough items available! Adjust your request number.", category='danger')
        else:
            teams = []    
            if user.inventory[itemName].get("Teams") == None:
                myTeam = current_user.name + "|" + str(itemNumber)
                teams = [myTeam]
            else:
                teams = user.inventory[itemName]["Teams"]               
                currentTeamCount = 0
                currentTeamPos = 0
                for t in teams:
                    teamList = t.split("|")
                    currentTeamPos += 1
                    if teamList[0] == current_user.name:
                        currentTeamCount = teamList[1]
                        break
                if int(currentTeamCount) > 0:
                    myTeam = current_user.name + "|" + str(itemNumber + int(currentTeamCount))
                    teams[currentTeamPos-1] = myTeam
                else:
                    myTeam = current_user.name + "|" + str(itemNumber)
                    teams.append(myTeam)
            availCount = availCount - itemNumber
            displayTeam = ""
            for t in teams:
                teamList = t.split("|")
                displayTeam += (teamList[0] + ": " + teamList[1] + "\n")
            user.inventory[itemName] = {
                "Name": itemName,
                "SKU" : itemSKU,
                "Count" : count,
                "AvailCount": availCount,
                "Teams":teams,
                "DisplayTeams":displayTeam
            }
                #for name in user.inventory.keys():
                #    invItems.append(user.inventory[name])
    db.session.add(current_user)
    db.session.commit()
    #return render_template("inventory.html", all_items = dataVal, inventory = invItems)
    return redirect(url_for('main.inventory'))

@main.route('/wishlist', methods=['POST'])
@login_required(role="ANY")
def wishlist_post():
    invItems = []
    manageForm = WLManageForm()
    managedItem = request.form.get("managed_item")
    requestor = request.form.get("requestor")
    print(requestor)
    if manageForm.orderSubmit.data:
        for name in current_user.wishlist_requests.keys():
            if name == managedItem:
                current_user.wishlist_requests[name]["Status"] = "Ordered"
            invItems.append(current_user.wishlist_requests[name])
        #now need to update requestor's wishlist page
        user = User.query.filter_by(email=requestor).first()
        user.wishlist_requests[managedItem]["Status"] = "Ordered"
        db.session.add(current_user)
        db.session.commit()
        return render_template("wishlist.html", all_items = dataVal, wishlist_requests = invItems, manage_form = manageForm)
    if manageForm.fulfilSubmit.data:
        managedItem = request.form.get("managed_item")
        for name in current_user.wishlist_requests.keys():
            if name == managedItem:
                current_user.wishlist_requests[name]["Status"] = "Fulfiled"
            invItems.append(current_user.wishlist_requests[name])
        user = User.query.filter_by(email=requestor).first()
        user.wishlist_requests[managedItem]["Status"] = "Fulfiled"
        db.session.add(current_user)
        db.session.commit()
        return render_template("wishlist.html", all_items = dataVal, wishlist_requests = invItems, manage_form = manageForm)
    if manageForm.declineSubmit.data:
        managedItem = request.form.get("managed_item")
        for name in current_user.wishlist_requests.keys():
            if name == managedItem:
                current_user.wishlist_requests[name]["Status"] = "Declined"
            invItems.append(current_user.wishlist_requests[name])
        user = User.query.filter_by(email=requestor).first()
        user.wishlist_requests[managedItem]["Status"] = "Declined"
        db.session.add(current_user)
        db.session.commit()
        return render_template("wishlist.html", all_items = dataVal, wishlist_requests = invItems, manage_form = manageForm)
    if manageForm.cancelSubmit.data:
        status = request.form.get("status")
        print(status)
        if status != "Requested":
            flash(f"You can only cancel Requested items!", category='danger')
        else:
            current_user.wishlist_requests[managedItem]["Status"] = "Cancelled"
            #for name in current_user.wishlist_requests.keys():
            #    invItems.append(current_user.wishlist_requests[name])
            coachEmail = ""
            for userEmail in current_user.received_requests.keys():
                if userEmail != current_user.email:
                    coachEmail = userEmail
            coach = User.query.filter_by(savedEmail=coachEmail).first()
            coach.wishlist_requests[managedItem]["Status"] = "Cancelled"
            db.session.add(current_user)
            db.session.commit()
        #return render_template("wishlist.html", all_items = dataVal, wishlist_requests = invItems, manage_form = manageForm)  
        return redirect(url_for('main.wishlist'))       
    if manageForm.deleteSubmit.data:
        managedItem = request.form.get("managed_item")
        status = request.form.get("status")
        print(status)
        if status == "Requested" or status == "Ordered":
            flash(f"You cannot delete Requested or Ordered items!", category='danger')
        else:
            del current_user.wishlist_requests[managedItem]
            for name in current_user.wishlist_requests.keys():
                invItems.append(current_user.wishlist_requests[name])
                db.session.add(current_user)
            db.session.commit()
        #return render_template("wishlist.html", all_items = dataVal, wishlist_requests = invItems, manage_form = manageForm)
        return redirect(url_for('main.wishlist'))
    itemName = request.form.get('selectItemName1')
    itemNumber = int(request.form.get('amountInserted1'))
    print(itemName)
    print(itemNumber)
    count = 0
    price = ""
    status = "Requested"
    for item in dataVal:
        if item["name"] and item["name"] == itemName:
            itemSKU = item["SKU"]
            price = "$" + str(item["price"])
        if item["SKU"] == itemName:
            itemSKU = itemName
            itemName = item["name"]
            price = "$" + str(item["price"])
    if (current_user.urole == "coach"):
        print("coach after urole")
        invItems = []
        if itemName in current_user.wishlist_requests:
            count = current_user.wishlist_requests[itemName]["Count"]
        count += itemNumber
        current_user.wishlist_requests[itemName] = {
            "Name": itemName,
            "SKU" : itemSKU,
            "Count" : count,
            "Price": price,
            "Team": "COACH",
            "Status": "Requested",
            "Requestor": current_user.email
        }
        for name in current_user.wishlist_requests.keys():
            invItems.append(current_user.wishlist_requests[name])

    elif (current_user.urole == "student" and current_user.confirmedRequests):
        invItems = []
        print("student after urole")
        coachEmail = ""
        for userEmail in current_user.received_requests.keys():
            if userEmail != current_user.email:
                coachEmail = userEmail
            if userEmail != current_user.email:
                continue
            user = User.query.filter_by(email=userEmail).first()
            if user.wishlist_requests == None:
                continue
            if itemName in user.wishlist_requests:
                count = user.wishlist_requests[itemName]["Count"]
            count += itemNumber
            if current_user.email == user.email:
                teamName = user.name               
                user.wishlist_requests[itemName] = {
                    "Name": itemName,
                    "SKU" : itemSKU,
                    "Count": count,
                    "Price": price,
                    "Team": teamName,
                    "Status": "Requested",
                    "Requestor": current_user.email
                }
            print("after continue")
            for name in user.wishlist_requests.keys():
                #invItems.append(user.wishlist_requests[name])
                invItems.append(user.wishlist_requests[name])
        # we now need to reflect the request in coach's wishlist
        print(coachEmail)
        coach = User.query.filter_by(savedEmail=coachEmail).first()
        coach.wishlist_requests[itemName] = {
                    "Name": itemName,
                    "SKU" : itemSKU,
                    "Count": count,
                    "Price": price,
                    "Team": current_user.name,
                    "Status": status,
                    "Requestor": current_user.email
        }

    db.session.add(current_user)
    db.session.commit()
    return render_template("wishlist.html", all_items = dataVal, wishlist_requests = invItems, manage_form = manageForm)
    
@main.route('/wishlist')
@login_required(role="ANY")
def wishlist():
    invItems = []
    manage_form = WLManageForm()
    if (current_user.urole == "coach"):  
        for name in current_user.wishlist_requests.keys():
            invItems.append(current_user.wishlist_requests[name])
    elif (current_user.urole == "student" and current_user.confirmedRequests):
        for studentEmail in current_user.received_requests.keys():
            #if current_user.received_requests[coachEmail]:
            user = User.query.filter_by(savedEmail=studentEmail).first()
            if current_user.email == user.email:
                for name in user.wishlist_requests.keys():
                    invItems.append(user.wishlist_requests[name])
    return render_template("wishlist.html", all_items = dataVal, wishlist_requests = invItems, manage_form = manage_form) 

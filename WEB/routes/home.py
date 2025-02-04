from WEB import *
from WEB.help_funcs import *


@app.route("/", methods=["GET", "POST"])
def home():
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    if request.method == "POST":
        email = request.form["email"]
        question = request.form["Question"]
        already_accounts = requests.get("http://127.0.0.1:5000/api/Accounts", )
        already_accounts = already_accounts.json()
        ok = None
        for already_account in already_accounts["message"]:
            if (already_account[2] == email
                    and already_account[4] == encode(question)
                    and already_account[1] == 5):
                ok = True
                password = already_account[4]
                email = already_account[2]
                user_name = already_account[3]
                rank = already_account[1]
                _id = already_account[0]
            elif (already_account[3] == email
                  and already_account[4] == encode(question)
                  and already_account[1] == 5):
                ok = True
                password = already_account[4]
                email = already_account[2]
                user_name = already_account[3]
                rank = already_account[1]
                _id = already_account[0]
        if ok is True:
            session["Is_Admin"] = True
            session["id"] = _id
            session["User Name"] = user_name
            session["Email"] = email
            session["Rank"] = rank
            session["Password"] = password
            return redirect("/Admin/")
        config = requests.post(
            "http://127.0.0.1:5000/api/Contact_Us",
            {
                "email": email,
                "question": question
            },
        )
        config = config.json()
        if config["message"] is True:
            try:
                session.pop("email")
                session.pop("question")
            except Exception as e:
                warnings.filterwarnings(e)
            flash(
                "Your Question will be answered as soon as possible by our team.",
                "success",
            )
            return redirect("/")
        session["email"] = email
        session["question"] = question
        flash("There is some error so please try again.", "danger")
        return redirect("/")
    password = "01x2253x6871"
    config = requests.get("http://127.0.0.1:5000/api/get_config",
                          {"password": password})
    config = config.json()
    return render_template(
        "home/home.html",
        gif_1=config["config"]["Home"]["Help you Learn Stuff"]["Gif"],
        gif_2=config["config"]["Home"]["About Us"]["Gif"],
        gif_3=config["config"]["Home"]["Contact Us"]["Gif"],
        description_1=config["config"]["Home"]["Help you Learn Stuff"]
        ["Description"],
        description_2=config["config"]["Home"]["About Us"]["Description"],
        description_3=config["config"]["Home"]["Contact Us"]["Description"],
        session=session,
    )


@app.route("/Sign/Up", methods=["GET", "POST"])
@app.route("/Sign/Up/", methods=["GET", "POST"])
def sign_up():
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    password = "01x2253x6871"
    config = requests.get("http://127.0.0.1:5000/api/get_config",
                          {"password": password})
    config = config.json()
    if request.method == "POST":
        email = request.form["Email"]
        password = request.form["Password"]
        user_name = request.form["User Name"]
        if verify_email(email) is False:
            flash("Invalid Email", "danger")
            return redirect("/Sign/Up")
        already_accounts = requests.get("http://127.0.0.1:5000/api/Accounts", )
        already_accounts = already_accounts.json()
        for already_account in already_accounts["message"]:
            if already_account[1] == email and already_account[3] == encode(
                    password):
                flash("Email is already exist.", "danger")
                return redirect("/Sign/Up")
            if already_account[2] == user_name and already_account[
                    3] == encode(password):
                flash("User Name is already exist.", "danger")
                return redirect("/Sign/Up")
        account_add = requests.post(
            "http://127.0.0.1:5000/api/Accounts",
            {
                "email": email,
                "password": encode(password),
                "user_name": user_name
            },
        )
        account_add = account_add.json()
        session["Email or User Name"] = email
        session["Password"] = password
        flash("Your account has been created.", "success")
        return redirect("/Sign/In")
        # session["2FACAUTH"] = True
    return render_template("home/sign_up.html", session=session, config=config)


@app.route("/Sign/In", methods=["GET", "POST"])
@app.route("/Sign/In/", methods=["GET", "POST"])
def sign_in():
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    password = "01x2253x6871"
    config = requests.get("http://127.0.0.1:5000/api/get_config",
                          {"password": password})
    config = config.json()
    if request.method == "POST":
        user_name_or_email = request.form["Email or User Name"]
        password = request.form["Password"]
        already_accounts = requests.get("http://127.0.0.1:5000/api/Accounts", )
        already_accounts = already_accounts.json()
        ok = None
        for already_account in already_accounts["message"]:
            if already_account[2] == user_name_or_email and already_account[
                    4] == encode(password):
                email = already_account[2]
                user_name = already_account[3]
                _id = already_account[0]
                rank = already_account[1]
                ok = True
            elif already_account[3] == user_name_or_email and already_account[
                    4] == encode(password):
                email = already_account[2]
                user_name = already_account[3]
                _id = already_account[0]
                rank = already_account[1]
                ok = True
        if ok is True:
            try:
                session.pop("Email or User Name")
                session.pop("Password")
            except Exception as e:
                warnings.filterwarnings(e)
            session["id"] = _id
            session["User Name"] = user_name
            session["Email"] = email
            session["Password"] = password
            session["Rank"] = rank
            flash("You have loged in successfully", "success")
            return redirect(f"/Usr/{_id}/")
        session["Email or User Name"] = user_name_or_email
        session["Password"] = password
        flash("Email or User Name and Password is wrong.", "danger")
        return redirect("/Sign/In")
        # session["2FACAUTH"] = False
    return render_template("home/sign_in.html", session=session, config=config)


# @app.route("/2/Fac/Auth/", methods=["POST", "GET"])
# @app.route("/2/Fac/Auth/", methods=["POST", "GET"])
# def sign_two_face_auth():
#     # try:
#     if "2FACAUTH" in session:
#         db = cluster["2FACAUTH"]
#         collection = db["2FACAUTH"]
#         if request.method == "POST":
#             email_code = request.form["email"]
#             phone_number_code = request.form["phone_number"]
#             # results = [
#             #     collection.find_one(
#             #         {
#             #             session["Email"]: int(email_code),
#             #             session["Phone Number"]: int(phone_number_code),
#             #             "user_name": session["User Name"],
#             #         }
#             #     )
#             # ]
#             results = ["GRG", "FEG"]
#             if results == [None]:
#                 flash("Email or Phone Number code is wrong.", "danger")
#                 return redirect("/Sign/In")
#             # collection.delete_one(results[0])
#             if session["2FACAUTH_TYPE"] is False:
#                 session["auth"] = True
#             session.pop("2FACAUTH")
#             return redirect(session["route"])
#         two_fac_auth(session["User Name"], session["Email"], session["Phone Number"])
#         return render_template("/home/2_fac_auth.html")

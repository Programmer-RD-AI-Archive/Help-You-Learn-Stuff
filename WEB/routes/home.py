from requests.sessions import session
from WEB import *


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        email = request.form["email"]
        question = request.form["Question"]
        config = requests.post(
            "http://127.0.0.1:5000/api/Contact_Us", {"email": email, "question": question}
        )
        config = config.json()
        print("*" * 50)
        print(config)
        print("*" * 50)
        if config["message"] is True:
            try:
                session.pop("email")
                session.pop("question")
            except:
                pass
            flash("Your Question will be answered as soon as possible by our team.", "success")
            return redirect("/")
        else:
            session["email"] = email
            session["question"] = question
            flash("There is some error so please try again.", "danger")
            return redirect("/")
    password = "01x2253x6871"
    config = requests.get("http://127.0.0.1:5000/api/get_config", {"password": password})
    config = config.json()
    return render_template(
        "home/home.html",
        gif_1=config["config"]["Home"]["Help you Learn Stuff"]["Gif"],
        gif_2=config["config"]["Home"]["About Us"]["Gif"],
        gif_3=config["config"]["Home"]["Contact Us"]["Gif"],
        description_1=config["config"]["Home"]["Help you Learn Stuff"]["Description"],
        description_2=config["config"]["Home"]["About Us"]["Description"],
        description_3=config["config"]["Home"]["Contact Us"]["Description"],
        session=session,
    )


@app.route("/Sign/Up", methods=["GET", "POST"])
def sign_up():
    password = "01x2253x6871"
    config = requests.get("http://127.0.0.1:5000/api/get_config", {"password": password})
    config = config.json()
    if request.method == "POST":
        email = request.form["Email"]
        password = request.form["Password"]
        user_name = request.form["User Name"]
        # remember_password = request.form["Remember Password"]  # TODO
        already_accounts = requests.get(
            "http://127.0.0.1:5000/api/Accounts",
        )
        already_accounts = already_accounts.json()
        for already_account in already_accounts:
            if already_account[1] == email and already_account[3] == encode(password):
                flash("Email is already exist.", "danger")
                return redirect("/Sign/Up")
            elif already_account[2] == user_name and already_account[3] == encode(password):
                flash("User Name is already exist.", "danger")
                return redirect("/Sign/Up")
        account_add = requests.post(
            "http://127.0.0.1:5000/api/Accounts",
            {"email": email, "password": encode(password), "user_name": user_name},
        )
        account_add = account_add.json()
        session["Email"] = email
        session["Password"] = encode(password)
        session["User_Name"] = user_name
        flash("Your account has been created.", "success")
        return redirect("/Sign/In")
    return render_template("home/sign_up.html", session=session, config=config)

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
    print(config)
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
    print(config)
    if request.method == "POST":
        pass
    return render_template("home/sign_up.html", session=session,config=config)

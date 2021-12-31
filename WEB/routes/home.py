from WEB import *


@app.route("/")
def home():
    if requests.method == "POST":
        email = requests.form['email']
        question = requests.form['Question']
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
    )

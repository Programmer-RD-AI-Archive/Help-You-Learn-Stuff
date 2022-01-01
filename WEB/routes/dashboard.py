from WEB import *
from WEB.help_funcs import *


@app.route("/Usr/<_id>", methods=["GET", "POST"])
@app.route("/Usr/<_id>/", methods=["GET", "POST"])
def usr_home(_id):
    if str(_id) == str(session["id"]):
        password = "01x2253x6871"
        config = requests.get("http://127.0.0.1:5000/api/get_config", {"password": password})
        config = config.json()
        return render_template("dashboard/home.html", session=session, config=config)

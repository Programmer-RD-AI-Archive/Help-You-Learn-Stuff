from WEB import *
from WEB.help_funcs import *


@app.route("/Usr/<_id>", methods=["GET", "POST"])
@app.route("/Usr/<_id>/", methods=["GET", "POST"])
def usr_home(_id):
    if str(_id) == str(session["id"]):
        password = "01x2253x6871"
        config = requests.get("http://127.0.0.1:5000/api/get_config", {"password": password})
        config = config.json()
        courses = requests.get(
            "http://127.0.0.1:5000/api/azure/sql",
            {"Query": f"SELECT * FROM Courses", "Type": "Select"},
        ).json()["message"]
        new_cources = []
        iter_cources = []
        idx = 0
        for cource in courses:
            if idx % 2 == 0:
                new_cources.append(iter_cources)
                iter_cources = []
            idx += 1
            iter_cources.append(cource)
        new_cources.append(iter_cources)
        return render_template(
            "dashboard/home.html", session=session, config=config, courses=new_cources
        )


@app.route("/Usr/<_id>/Log/Out", methods=["GET", "POST"])
@app.route("/Usr/<_id>/Log/Out/", methods=["GET", "POST"])
def usr_logout(_id):
    if str(_id) == str(session["id"]):
        session.pop("id", None)
        session.pop("User Name", None)
        session.pop("Email", None)
        session.pop("Password", None)
        session.pop("type", None)
        flash("Logged Out", "success")
        return redirect("/")

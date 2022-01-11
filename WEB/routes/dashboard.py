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
        new_cources = new_cources[1:]
        return render_template(
            "dashboard/home.html", session=session, config=config, courses=new_cources, id_user=_id
        )


@app.route("/Usr/<_id>/Cources/<course_id>/", methods=["GET", "POST"])
@app.route("/Usr/<_id>/Cources/<course_id>", methods=["GET", "POST"])
def usr_home_cources(_id, course_id):
    if str(_id) == str(session["id"]):
        password = "01x2253x6871"
        config = requests.get("http://127.0.0.1:5000/api/get_config", {"password": password})
        config = config.json()
        courses = requests.get(
            "http://127.0.0.1:5000/api/azure/sql",
            {"Query": f"SELECT * FROM Courses WHERE ID={course_id}", "Type": "Select"},
        ).json()["message"]
        info = courses[0][2]
        info = requests.get(
            "http://127.0.0.1:5000/api/azure/storage",
            {"Type": "Download File", "Container Name": "cource", "file_name": info},
        ).json()["message"]
        info = dict(eval(info))
        session[f"Cource {course_id}"] = info
        next_lesson = list(info.keys())[0]
        # TODO check if length of cource is higher than 1
        return redirect(f"/Usr/{_id}/Cources/{course_id}/Lesson/{next_lesson}")


@app.route("/Usr/<_id>/Cources/<course_id>/Lesson/<lesson_id>/", methods=["GET", "POST"])
@app.route("/Usr/<_id>/Cources/<course_id>/Lesson/<lesson_id>", methods=["GET", "POST"])
def usr_home_cource_lesson(_id, course_id, lesson_id):
    if str(_id) == str(session["id"]):
        if int(lesson_id) <= len(session[f"Cource {course_id}"]):
            specific_lesson_info = session[f"Cource {course_id}"][lesson_id]
            print(specific_lesson_info)
            courses = requests.get(
                "http://127.0.0.1:5000/api/azure/sql",
                {"Query": f"SELECT * FROM Courses WHERE ID={course_id}", "Type": "Select"},
            ).json()["message"]
            # next_lesson = info.keys()[0]
            # TODO check if length of cource is higher than 1
            return render_template()
        return redirect(f"/Usr/{_id}")


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

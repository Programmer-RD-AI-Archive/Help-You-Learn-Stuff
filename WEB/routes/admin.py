from bs4 import Tag, BeautifulSoup
from requests.sessions import session
from WEB import *
from WEB.help_funcs import *

link_of_resource_dict = {1: "Video", 2: "Image", 3: "Sound", 4: "Website"}


@app.route("/Admin", methods=["GET", "POST"])
@app.route("/Admin/", methods=["GET", "POST"])
def admin_home():
    if "Is_Admin" in session:
        config = requests.get("http://127.0.0.1:5000/api/get_config", {"password": password})
        config = config.json()
        return render_template("admin/home.html", config=config, session=session)


@app.route("/Admin/Question", methods=["GET", "POST"])
@app.route("/Admin/Question/", methods=["GET", "POST"])
def admin_question():
    if "Is_Admin" in session:
        print(session)
        return render_template("admin/question.html", config=config, session=session)


@app.route("/Admin/Resources", methods=["GET", "POST"])
@app.route("/Admin/Resources/", methods=["GET", "POST"])
def admin_resources():
    if "Is_Admin" in session:
        if request.method == "POST":
            method_of_resource = request.form["method-of-resource"]
            link_of_resource = request.form["link-of-resource"]
            title = request.form["Title"]
            description = request.form["Description"]
            results = requests.put(
                "http://127.0.0.1:5000/api/resources",
                {
                    "method_of_resource": method_of_resource,
                    "link_of_resource": link_of_resource,
                    "title": title,
                    "description": description,
                },
            ).json()
            flash("Resource Added", "success")
            print(results)
            return redirect("/Admin/Resources")
        results = requests.get(
            "http://127.0.0.1:5000/api/resources",
        ).json()
        return render_template(
            "admin/resources.html",
            session=session,
            resources=results["message"],
            link_of_resource_dict=link_of_resource_dict,
        )


@app.route(
    "/Admin/Resources/<_id>/Delete/",
    methods=["GET", "POST"],
)
@app.route(
    "/Admin/Resources/<_id>/Delete",
    methods=["GET", "POST"],
)
def admin_resources_delete(_id):
    if "Is_Admin" in session:
        results = requests.post(
            "http://127.0.0.1:5000/api/resources",
            {
                "id": int(_id),
            },
        )
        flash("Deleted", "success")
        return redirect("/Admin/Resources")


@app.route(
    "/Admin/Resources/<_id>/Edit/",
    methods=["GET", "POST"],
)
@app.route(
    "/Admin/Resources/<_id>/Edit",
    methods=["GET", "POST"],
)
def admin_resources_edit(_id):
    if "Is_Admin" in session:
        if request.method == "POST":
            method_of_resource = request.form["method-of-resource"]
            link_of_resource = request.form["link-of-resource"]
            title = request.form["Title"]
            description = request.form["Description"]
            results = requests.get(
                "http://127.0.0.1:5000/api/azure/sql",
                {
                    "Query": f"UPDATE Resources SET method_of_resource={method_of_resource}, link_of_resource={link_of_resource}, title={title}, description={description}",
                    "Type": "Insert",
                },
            ).json()
            print(results)
            flash("Updated resources", "success")
            return redirect("/Admin/Resources")
        results = requests.get(
            "http://127.0.0.1:5000/api/azure/sql",
            {"Query": f"SELECT * FROM Resources WHERE ID = {_id}", "Type": "Select"},
        ).json()["message"][0]
        print(results)
        return render_template(
            "admin/resources.html",
            method_of_resource=str(results[1]),
            link_of_resource=results[2],
            description=results[3],
            title=results[4],
        )


@app.route("/Admin/Question/Post", methods=["POST"])
@app.route("/Admin/Question/Post/", methods=["POST"])
def admin_question_post():
    flash("Question Added", "success")
    request_form = eval(list(dict(request.form).keys())[0] + list(dict(request.form).values())[0])
    info = request_form["info"]
    yourdiv = request_form["yourdiv"]
    name = info["name"]
    del info["name"]
    print(info)
    soup = BeautifulSoup(yourdiv, "html.parser")
    for idx in range(len(info)):
        idx = idx + 1
        element = soup.find("input", id=f"{idx}-Input-Name")
        try:
            element.replaceWith(info[str(idx)][0])
        except:
            pass
        element = soup.find("button")
        try:
            element.string = ""
        except:
            pass
        try:
            element.unwrap()
        except:
            pass  # TODO Change Make if else statment
        element = soup.find("div", id=f"{idx}")
        try:
            del element.attrs['class"mb-3"']
        except:
            pass
        try:
            element.attrs["class"] = "mb-3"
        except:
            pass
        inputs = soup.find_all("input", id=f"{idx}-Label")
        print(inputs)
        print("\n")
        for input_ in inputs:
            print(input_.attrs)
            print("\n")
            input_.attrs["answer"] = info[str(idx)][1]
            input_.attrs["name"] = input_.attrs["id"]
    returned_vals = requests.post(
        "http://127.0.0.1:5000/api/cources", {"html": str(soup), "name": name}
    )
    print(returned_vals)
    return ("", 200)


@app.route("/Admin/Test")
def admin_test():
    return render_template("admin/test.html")


@app.route("/Admin/Log/Out", methods=["GET", "POST"])
@app.route("/Admin/Log/Out/", methods=["GET", "POST"])
def admin_log_out():
    if "Is_Admin" in session:
        session.pop("Is_Admin")
        session.pop("id")
        session.pop("User Name")
        session.pop("Email")
        session.pop("Rank")
        session.pop("Password")
        flash("Loged out as admin", "success")
        return redirect("/")

import ast
from WEB import *
from WEB.help_funcs import *

link_of_resource_dict = {1: "Video", 2: "Image", 3: "Sound", 4: "Website"}


@app.route("/Admin", methods=["GET", "POST"])
@app.route("/Admin/", methods=["GET", "POST"])
def admin_home():
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    if "Is_Admin" in session:
        config = requests.get("http://127.0.0.1:5000/api/get_config",
                              {"password": password})
        config = config.json()
        return render_template(
            "admin/home.html",
            config=config,
            session=session,
        )
    return abort(404)


@app.route("/Admin/Courses", methods=["GET", "POST"])
@app.route("/Admin/Courses/", methods=["GET", "POST"])
def admin_courses():
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    if "Is_Admin" in session:
        resources = requests.get(
            "http://127.0.0.1:5000/api/azure/sql",
            {
                "Query": "SELECT * FROM Resources",
                "Type": "Select"
            },
        ).json()["message"]
        questions = requests.get(
            "http://127.0.0.1:5000/api/azure/sql",
            {
                "Query": "SELECT * FROM Questions",
                "Type": "Select"
            },
        ).json()["message"]
        courses = requests.get(
            "http://127.0.0.1:5000/api/azure/sql",
            {
                "Query": "SELECT * FROM Courses",
                "Type": "Select"
            },
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
            "admin/courses.html",
            resources=resources,
            questions=questions,
            courses=new_cources,
        )
    return abort(404)


@app.route("/Admin/Courses/Post/", methods=["GET", "POST"])
@app.route("/Admin/Courses/Post", methods=["GET", "POST"])
def admin_courses_post():
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    if "Is_Admin" in session:
        request_forms = request.form
        request_forms = dict(request_forms)
        new_request_forms = ""
        for key, val in zip(request_forms.keys(), request_forms.values()):
            new_request_forms += key
            new_request_forms += val
        request_forms = ast.literal_eval(new_request_forms)
        whole_content = request_forms["whole_content"]
        whole_content = BeautifulSoup(whole_content, "html.parser")
        info = request_forms["info"]
        image = request_forms["image"]
        name = request_forms["name"]
        marks = request_forms["marks"]
        response = requests.put(
            "http://127.0.0.1:5000/api/courses",
            {
                "whole_content": str(whole_content),
                "info": str(info),
                "image": str(image),
                "name": str(name),
                "marks": str(marks),
            },
        ).json()
        flash("Cources added", "success")
        return redirect("/Admin/Courses")
    return abort(404)


@app.route("/Admin/Question", methods=["GET", "POST"])
@app.route("/Admin/Question/", methods=["GET", "POST"])
def admin_question():
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    if "Is_Admin" in session:
        returned_vals = requests.get(
            "http://127.0.0.1:5000/api/questions").json()
        returned_vals = returned_vals["message"]
        return render_template(
            "admin/question.html",
            config=config,
            session=session,
            questions=returned_vals,
        )
    return abort(404)


@app.route("/Admin/Resources", methods=["GET", "POST"])
@app.route("/Admin/Resources/", methods=["GET", "POST"])
def admin_resources():
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
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
            return redirect("/Admin/Resources")
        results = requests.get("http://127.0.0.1:5000/api/resources", ).json()
        return render_template(
            "admin/resources.html",
            session=session,
            resources=results["message"],
            link_of_resource_dict=link_of_resource_dict,
        )
    return abort(404)


@app.route(
    "/Admin/Resources/<_id>/Delete/",
    methods=["GET", "POST"],
)
@app.route(
    "/Admin/Resources/<_id>/Delete",
    methods=["GET", "POST"],
)
def admin_resources_delete(_id):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    if "Is_Admin" in session:
        results = requests.post(
            "http://127.0.0.1:5000/api/resources",
            {
                "id": int(_id),
            },
        )
        flash("Deleted", "success")
        return redirect("/Admin/Resources")
    return abort(404)


@app.route(
    "/Admin/Resources/<_id>/Edit/",
    methods=["GET", "POST"],
)
@app.route(
    "/Admin/Resources/<_id>/Edit",
    methods=["GET", "POST"],
)
def admin_resources_edit(_id):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    if "Is_Admin" in session:
        if request.method == "POST":
            method_of_resource = request.form["method-of-resource"]
            link_of_resource = request.form["link-of-resource"]
            title = request.form["Title"]
            description = request.form["Description"]
            # "UPDATE Resources SET title='ttt' WHERE ID=7;"
            results = requests.get(
                "http://127.0.0.1:5000/api/azure/sql",
                {
                    "Query":
                    f"UPDATE Resources SET method_of_resource='{method_of_resource}', link_of_resource='{link_of_resource}', title='{title}', description='{description}' WHERE ID={_id}",
                    "Type": "Insert",
                },
            ).json()
            flash("Updated resources", "success")
            return redirect("/Admin/Resources")
        results = requests.get(
            "http://127.0.0.1:5000/api/azure/sql",
            {
                "Query": f"SELECT * FROM Resources WHERE ID = {_id}",
                "Type": "Select"
            },
        ).json()["message"][0]
        return render_template(
            "admin/resources.html",
            method_of_resource=str(results[1]),
            link_of_resource=results[2],
            description=results[3],
            title=results[4],
        )
    return abort(404)


@app.route("/Admin/Question/Post", methods=["POST"])
@app.route("/Admin/Question/Post/", methods=["POST"])
def admin_question_post():
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    flash("Question Added", "success")
    request_form = ast.literal_eval(
        list(dict(request.form).keys())[0] +
        list(dict(request.form).values())[0])
    info = request_form["info"]
    yourdiv = request_form["yourdiv"]
    name = info["name"]
    del info["name"]
    soup = BeautifulSoup(yourdiv, "html.parser")
    for idx in range(len(info)):
        idx = idx + 1
        element = soup.find("input", id=f"{idx}-Input-Name")
        try:
            element.replaceWith(info[str(idx)][0])
        except Exception as e:
            warnings.filterwarnings(e)
        element = soup.find("button")
        try:
            element.string = ""
        except Exception as e:
            warnings.filterwarnings(e)
        try:
            element.unwrap()
        except Exception as e:
            warnings.filterwarnings(e)  # TODO Change Make if else statment
        element = soup.find("div", id=f"{idx}")
        try:
            del element.attrs['class"mb-3"']
        except Exception as e:
            warnings.filterwarnings(e)
        try:
            element.attrs["class"] = "mb-3"
        except Exception as e:
            warnings.filterwarnings(e)
        element = soup.find("hr")
        element.unwrap()
        inputs = soup.find_all("input", id=f"{idx}-Label")
        for input_ in inputs:
            input_.attrs["answer"] = info[str(idx)][1]
            input_.attrs["name"] = input_.attrs["id"]
    returned_vals = requests.post("http://127.0.0.1:5000/api/questions", {
        "html": str(soup),
        "name": str(name)
    }).json()
    return ("", 200)


@app.route("/Admin/Question/<_id>/Preview/")
@app.route(
    "/Admin/Question/<_id>/Preview", )
def admin_question_preview(_id):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    if "Is_Admin" in session:
        results = requests.get(
            "http://127.0.0.1:5000/api/azure/sql",
            {
                "Query": f"SELECT * FROM Questions WHERE ID = {_id}",
                "Type": "Select"
            },
        ).json()["message"][0]
        return render_template("admin/admin_question_preview.html",
                               code=results[1])
    return abort(404)


@app.route("/Admin/Question/<_id>/Delete/")
@app.route(
    "/Admin/Question/<_id>/Delete", )
def admin_question_delete(_id):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    if "Is_Admin" in session:
        results = requests.get(
            "http://127.0.0.1:5000/api/azure/sql",
            {
                "Query": f"DELETE FROM Questions WHERE ID={_id}",
                "Type": "Insert"
            },
        ).json()
        flash("Deleted", "success")
        return redirect("/Admin/Question")
    return abort(404)


@app.route("/Admin/Test")
def admin_test():
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    return render_template("admin/test.html")


@app.route("/Admin/Log/Out", methods=["GET", "POST"])
@app.route("/Admin/Log/Out/", methods=["GET", "POST"])
def admin_log_out():
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    if "Is_Admin" in session:
        session.pop("Is_Admin")
        session.pop("id")
        session.pop("User Name")
        session.pop("Email")
        session.pop("Rank")
        session.pop("Password")
        flash("Loged out as admin", "success")
        return redirect("/")
    return abort(404)

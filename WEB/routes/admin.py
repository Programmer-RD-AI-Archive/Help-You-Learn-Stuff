from bs4 import Tag, BeautifulSoup
from requests.sessions import session
from WEB import *
from WEB.help_funcs import *


@app.route("/Admin", methods=["GET", "POST"])
@app.route("/Admin/", methods=["GET", "POST"])
def admin_home():
    if "Is_Admin" in session:
        config = requests.get("http://127.0.0.1:5000/api/get_config", {"password": password})
        config = config.json()
        return render_template("admin/home.html", config=config, session=session)


@app.route("/Admin/Courses", methods=["GET", "POST"])
@app.route("/Admin/Courses/", methods=["GET", "POST"])
def admin_courses():
    if "Is_Admin" in session:
        print(session)
        return render_template("admin/courses.html", config=config, session=session)


@app.route("/Admin/Courses/Post", methods=["POST"])
@app.route("/Admin/Courses/Post/", methods=["POST"])
def admin_courses_post():
    flash("Question Added", "success")
    request_form = eval(list(dict(request.form).keys())[0] + list(dict(request.form).values())[0])
    info = request_form["info"]
    yourdiv = request_form["yourdiv"]
    soup = BeautifulSoup(yourdiv, "html.parser")
    for idx in range(len(info)):
        idx = idx + 1
        element = soup.find('input',id=f"{idx}-Input-Name")
        element.replaceWith(info[str(idx)][0])
        element = soup.find("button")
        element.string = ""
        element.unwrap()
        element = soup.find("div", id=f"{idx}")
        print(element)
        print("\n")
        print(element.attrs)
        print("\n")
        try:
            del element.attrs['class"mb-3"']
        except:
            pass
        element.attrs["class"] = "mb-3"
    print(soup)
    print("\n")
    print(info)
    return ("", 200)


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

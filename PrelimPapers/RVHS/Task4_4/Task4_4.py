import flask, sqlite3
from flask import render_template
app = flask.Flask(__name__)

@app.route("/")
def main():
    client = sqlite3.connect("../invigilation.db")

    curr = client.execute("SELECT Teacher.Name, ExamDuty.Role, COUNT(*) FROM ExamDuty INNER JOIN Teacher ON Teacher.TeacherID = ExamDuty.TeacherID GROUP BY Name, Role;")
    attr = list(curr)
    return render_template("display.html", attr = attr)


if __name__ == "__main__":
    app.run()

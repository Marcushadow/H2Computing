import flask, sqlite3
from flask import render_template
app = flask.Flask(__name__)

@app.route("/")
def main():
    client = sqlite3.connect("../invigilation.db")

    curr = client.execute("SELECT Teacher.Name, ExamDuty.Role, COUNT(*) FROM ExamDuty INNER JOIN Teacher ON Teacher.TeacherID = ExamDuty.TeacherID GROUP BY Name, Role;")
    attr = list(curr)
    return render_template("display.html", attr = attr)

@app.route("/find/<name>")
def findTeacher(name):

    client = sqlite3.connect("../invigilation.db")
    curr = client.execute("SELECT ExamSession.SubjectName, ExamSession.PaperNo, ExamDuty.Role, Venue.VenueID, ExamSession.Date, ExamSession.StartTime, ExamSession.EndTime FROM ExamSession INNER JOIN ExamDuty ON ExamDuty.ExamSessionID = ExamSession.ExamSessionID INNER JOIN Teacher ON Teacher.TeacherID = ExamDuty.TeacherID INNER JOIN Venue ON Venue.VenueID = ExamSession.VenueID WHERE Teacher.Name = ?;", (name,))
    attr = list(curr)
    return render_template("teacher.html", attr = attr)


if __name__ == "__main__":
    app.run()

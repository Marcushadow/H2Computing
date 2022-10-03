import flask, sqlite3, os
from flask import send_from_directory, render_template, request
from werkzeug.utils import secure_filename

app = flask.Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/synthesis", methods = ["POST"])
def synthesis():
    if(request.method == "POST"):
        if(request.files and request.files["File"]):
            fileObj = request.files["File"]
        Name = request.form.get("Name")
        Caption = request.form.get("Caption")

        Filename = secure_filename(fileObj.filename)
        saveDirectory = os.path.join("pictures", Filename)
        fileObj.save(saveDirectory)
        
        client = sqlite3.connect("photos.db")
        curr = client.execute("INSERT INTO Photo (Name, Filename, Caption) VALUES (?,?,?)", (Name, Filename, Caption))
        client.commit()
        client.close()
        

    
    return render_template("index.html")

@app.route("/files")
def seeFiles():
    client = sqlite3.connect("photos.db")
    curr = client.execute("SELECT Name, Filename, Caption FROM Photo")
    attr = list(curr)
    client.close()

    return render_template("files.html", attr = attr)

@app.route("/photos/<filename>")
def getFile(filename):
    return send_from_directory("pictures", filename)

if __name__ == "__main__":
    app.run()

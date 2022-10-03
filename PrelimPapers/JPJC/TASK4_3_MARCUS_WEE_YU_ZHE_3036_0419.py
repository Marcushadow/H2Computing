import flask, sqlite3
from flask import render_template, request

app = flask.Flask(__name__)
emailStored = ""

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/validate", methods = ["POST"])
def synthesis():
    if(request.method == "POST"):
        global emailStored
        emailStored = request.form.get("Email")

        client = sqlite3.connect("JPFashion.db")
        curr = client.execute("SELECT Email FROM Customer");
        emailList = list(curr)
        for i in range(len(emailList)):
            emailList[i] = emailList[i][0]
        print(emailList)
            
        if(emailStored in emailList):
            return render_template("emailReenter.html")

        else:
            return render_template("secondaryForm.html")
        

@app.route("/loginValidate",  methods = ["POST"])
def successLogin():
    if(request.method == "POST"):
        global emailStored
        receivedEmail = request.form.get("Email")

        print(receivedEmail,"+", emailStored)

        if(receivedEmail == emailStored):
            return render_template("output.html", msg = "Successful login")

    return render_template("output.html", msg = "Unsuccessful login")


@app.route("/createAccount", methods = ["POST"])        
def createAcc():
    if(request.method == "POST"):
        fn = request.form.get("FirstName")
        ln = request.form.get("LastName")
        cn = request.form.get("Contact")
        dob = request.form.get("DOB")
        addr = request.form.get("Addr")

        client = sqlite3.connect("JPFashion.db")
        curr = client.execute("INSERT INTO Customer (Email, FirstName, LastName, ContactNumber, DOB, Address) VALUES (?,?,?,?,?,?)", (emailStored, fn, ln, cn, dob, addr))
        
        client.close()

    return render_template("output.html", msg = "Successfully created account")



if __name__== "__main__":
    app.run()

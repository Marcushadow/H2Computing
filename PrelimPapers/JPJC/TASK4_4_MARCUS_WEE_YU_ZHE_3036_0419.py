import flask, sqlite3
from flask import render_template, request

app = flask.Flask(__name__)

@app.route("/")
def main():
    return render_template("rentalsdue.html")

@app.route("/createAccount", methods = ["POST"])        
def sortRentals():
    if(request.method == "POST"):
        EndDate = request.form.get("EndDate")
        client = sqlite3.connect("JPFashion.db")
        curr = client.execute("SELECT ProductRental.ID, ProductRental.CatalogueNumber, CustomerRental.Email, Customer.ContactNumber FROM Customer INNER JOIN CustomerRental ON Customer.Email = CustomerRental.Email INNER JOIN ProductRental ON CustomerRental.ID = ProductRental.ID WHERE CustomerRental.EndDate = ? AND ProductRental.Returned = 'FALSE';", (EndDate,))
        attr = list(curr)
        client.close()

    return render_template("displayRentals.html", attr = attr)



if __name__== "__main__":
    app.run()

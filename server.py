from flask import Flask, redirect,request,render_template
from user import User
app=Flask(__name__)

@app.route("/")
def usersindex():
    users=User.get_all()
    return render_template("read.html",users=users)

@app.route("/new")
def newindex():
    return render_template("create.html")

@app.route("/createnew", methods=["post"])
def createnew():
    data={
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"]
    }
    print(data)
    User.save(data)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
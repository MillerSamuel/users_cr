from flask import Flask, redirect,request,render_template
from user import User
app=Flask(__name__)

@app.route("/")
def start():
    return redirect("/users")

@app.route("/users")
def usersindex():
    users=User.get_all()
    return render_template("read.html",users=users)

@app.route("/users/new")
def newindex():
    return render_template("create.html")

@app.route("/users/createnew", methods=["post"])
def createnew():
    data={
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"]
    }
    print(data)
    User.save(data)
    return redirect("/users")

@app.route("/users/edit/<int:id>")
def edit(id):
    data={
        "id":id
    }
    return render_template ("edit.html",user=User.get_one(data))

@app.route("/users/show/<int:id>")
def show(id):
    data={
        "id":id
    }
    return render_template("readone.html",user=User.get_one(data))

@app.route("/users/update",methods=["post"])
def update():
    User.update(request.form)
    return redirect("/users")

@app.route("/users/delete/<int:id>")
def delete(id):
    data={
        "id":id
    }
    print("deleting maybe")
    User.delete(data)
    return redirect("/users")


if __name__ == "__main__":
    app.run(debug=True)
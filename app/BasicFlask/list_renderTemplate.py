from flask import Flask,render_template
app=Flask(__name__)

@app.route("/")
#def index():
#    lst=["Dhiraj!","Daneil","Beautiful day in Sri Lanka!","Amar","Avengers was so cool!"]
#    return render_template("tmp1.html", name=lst)

def ind():
    user={"username":"Dhiraj"}
    posts=[
        {"author": {"username":"Daneil"},
         "body":"Beautiful day in Sri Lanka!"},
        {"author": {"username":"Amar"},
         "body":"Avengers was so cool!"}
        ]
    return render_template("tmp1.html", user=user,posts=posts)

if __name__=="__main__":
    app.run(debug=True)

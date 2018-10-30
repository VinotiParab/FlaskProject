from flask import Flask,render_template
app=Flask(__name__)

@app.route("/")
def index():
    string="Python FLASK workshop"
    return render_template("tmp.html", name=string)

def dict1():
    dict1={1:"vinoti",2:"shraddha",3:"archana"}
    return render_template("tmp.html", dict1=dict1)

def tup():
    tup=("devshree","sharvani","pramod")
    return render_template("tmp.html", tup=tup)
   

if __name__ == "__main__":
    app.run(debug=True)

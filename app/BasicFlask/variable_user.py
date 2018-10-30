from flask import Flask
app=Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/Variable/<name>")
def String(name):
    return "String is %s"%name

@app.route("/Variable/<number>")
def Int(number):
    return "Integer is %i"%number

@app.route("/Variable/<decimal>")
def Float(decimal):
    return "Float value is %f"%decimal

if __name__ == "__main__":
    app.run(debug=True)

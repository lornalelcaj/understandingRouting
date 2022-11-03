from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello world"

@app.route('/dojo')
def dojo():
    return "Dojo"

@app.route('/say/<name>')
def sayName(name):
    return f"Hello{name}"

@app.route('/repeat/<int:n>/string:s')
def repeat(n,s):
    x=' '
    for i in range (0,n):
        x+=f"<p>{s}</p>"
    return x

if __name__=="__main__":
    app.run(debug=True)
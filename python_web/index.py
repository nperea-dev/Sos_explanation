from flask import Flask, render_template

#app = Flask("python_web")
app=Flask(__name__,template_folder='templates')
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/inercia")
def inercia():
    return render_template("inercia.html")

"""
@app.route("/videos")
def Videostatic():
    return  render_template("videos.html")

"""

if __name__ == "__main__":
    app.run(debug=True)

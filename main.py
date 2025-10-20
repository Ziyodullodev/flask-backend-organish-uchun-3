from flask import Flask, render_template

app = Flask("__name__")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/iskandar")
def iskandar():
    return render_template("iskandar.html")


@app.route("/abdurahmon")
def abdurahmon():
    return render_template("abdurahmon.html")


@app.route("/diyorbek")
def diyorbek():
    return render_template("tigr.html")

@app.route("/iqbola")
def iqbola():
    return render_template("iqbola.html")

if __name__ == '__main__':
    app.run(debug=True)
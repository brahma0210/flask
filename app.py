from flask import Flask, render_template, flash

app = Flask(__name__)
app.secret_key = b'_3#u2J"d7h4\m\cdf]/'

@app.route('/')
def dashboard():
    flash("warning")
    flash("this is an invalid login")
    flash("error")
    return render_template("oops.html")


if __name__ == 'main':
    app.run()
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap5 import Bootstrap

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[
        DataRequired(), 
        Email(message="invalid email adress", check_deliverability=True)
    ])
    password = PasswordField(label='Password', validators=[
        DataRequired(),
        Length(min=8, message="Invalid password")
    ])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"
bootstrap = Bootstrap(app)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
                return render_template("success.html")
        else:
                return render_template("denied.html")
    return render_template("login.html", form=login_form)

@app.context_processor
def inject_bootstrap():
    return dict(bootstrap=bootstrap)


if __name__ == '__main__':
    app.run(debug=True)

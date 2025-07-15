from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
    '<p>This is a paragraph.</p>' \
    '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExNzJ2MW52dmI0c2R5anJyNnd3M3Zwb2ZrZmQ0bGFtOWswMjg5azU5biZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/M5rdwi1tNAXqU/giphy.gif" width=200px>'

@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye"

if __name__ == "__main__":
    app.run(debug=True)
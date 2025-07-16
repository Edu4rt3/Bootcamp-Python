from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)

blog_response = requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()
blog_data = []
for post in blog_response:
    blog_post = Post(post['id'], post['body'], post['title'], post['subtitle'])
    blog_data.append(blog_post)


@app.route('/')
def home():
    return render_template('index.html', blog=blog_data)


@app.route('/blog/<int:num_id>')
def get_post(num_id):
    return render_template('post.html', blog=blog_data, num=num_id)


if __name__ == '__main__':
    app.run(debug=True)
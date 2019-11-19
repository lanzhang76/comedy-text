from flask import Flask, escape, url_for, render_template

app = Flask(__name__)

post = [{
		'text': "How can a person be honest when they are so afraid of something that is happening to them? I’m not really sure how a person can be honest when they are so afraid of something that is happening to them. It doesn’t exist.” There’s no such thing as fear. There’s no such thing as fear. "
		},
		{'text':" love. Save my name, email, and website in this browser for the next time I comment."
		}]

@app.route('/')
def index():
    return render_template('index.html', posts = post);

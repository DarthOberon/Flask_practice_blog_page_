from flask import Flask, render_template, url_for
app =Flask(__name__)

posts =[
    {
        'author': 'Aryan Sharma',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'February 08, 2025'
    },
    {
        'author': 'John Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'February 09, 2025'
    
    }

]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hello.html', list_names = ['apple','banana','candy'])

@app.route("/<string:name>")
def green(name):
    return f'Hello {name}'

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
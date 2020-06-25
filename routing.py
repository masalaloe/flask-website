from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/home')
@app.route('/')
def _index():
    return render_template("home.html",
                            title='Home')

@app.route('/about')
def _about():
    return render_template('about.html',
                            title='About')

                            
@app.route('/project')
def _project():
    return render_template('project.html',
                            title='Project')



app.run(debug=True)
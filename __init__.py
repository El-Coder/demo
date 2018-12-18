from flask import Flask, render_template, flash, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://user:password@db:5432/db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'supersecretkey'


from model import db, Users
db.init_app(app)


@app.before_first_request
def initialize_database():
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if not request.form['first_name'] or not request.form['last_name']:
            return input_not_found()
        else:
            User = Users(request.form['first_name'], request.form['last_name'])
            db.session.add(User)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('home.html', Users=Users.query.all())


@app.errorhandler(404)
def input_not_found():
    return "Text fields cannot be empty please go back", 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

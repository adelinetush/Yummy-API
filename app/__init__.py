from flask import Flask

app = Flask(__name__)

@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)

from app.models import db




POSTGRES = {
    'user': 'ihvgbhmozzsovk',
    'pw': '5787a5a36454aae785e45bf65eecb700ebd5c3ad3f98e5bc38980f5ce8a3bd33',
    'db': 'dcfqo2tdioauli',
    'host': 'ec2-107-21-248-177.compute-1.amazonaws.com',
    'port': '5432',
}
POSTGRESTEST = {
    'user': 'postgres',
    'pw': 'root',
    'db': 'yummy',
    'host': 'localhost',
    'port': '5432',
}


# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/yummy'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRESTEST

db.init_app(app)

from app import views

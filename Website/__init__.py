from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = '93ea43c944bf4571941c7c2cfea8f51b'
from Website import routes
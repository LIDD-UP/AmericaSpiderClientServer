from flask import Flask



app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
app.config.from_pyfile('app.conf')
app.secret_key = 'bluesli'


from AmericaSpiderClientServer import views, models
from flask import Flask, rendertemplate
import config
from models import Trail

app = config.connexapp
app.addapi(config.basedir / 'swagger.yml') 
@app.route('/')

def home():
    return rendertemplate('home.html', trails = Trail.query.all())

if __name__ == '__main':
    app.run(host='0.0.0.0',port=8000,debug=True)
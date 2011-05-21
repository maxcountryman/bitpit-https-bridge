from flask import Flask
app = Flask(__name__)
app.config.from_object('httpstobitpit.config.Config') # use config.py

import httpstobitpit.views

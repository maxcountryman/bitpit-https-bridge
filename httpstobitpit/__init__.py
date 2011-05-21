from flask import Flask
app = Flask(__name__)
app.config.from_object('httpstobitpit.config.Config')

import httpstobitpit.views

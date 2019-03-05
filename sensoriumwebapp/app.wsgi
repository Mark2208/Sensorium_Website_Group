#! /usr/bin/python3.6

import sys
sys.path.insert(0, '/usr/local/env/myApp/')

#/var/www/html/Sensorium_Website_Group$

activate_this = '/var/www/html/Sensorium_Website_Group$/sensoriumwebapp/app.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

from app.myApp import app as application

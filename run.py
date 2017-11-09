#!flask/bin/python
# 
import os 
from app import app
import datetime

#app.run(debug=True)
port = int(os.environ.get('PORT',5000))
if(__name__=="__main__"):
    app.config['DEBUG'] = True

    app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(days=4)

    app.debug = True
    app.run(host='0.0.0.0',port=port)

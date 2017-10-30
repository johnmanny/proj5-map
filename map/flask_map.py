"""
Author: John Nemeth
Sources: heavy reference from previous CIS322 projects, written by U of O CIS dept. staff (Michal Young)
Description: Driver Program for flask server of leaflet implemented map
"""

import flask
from flask import request
import config
import dataprocess

##########
# globals
##
app = flask.Flask(__name__)
#loaded from credentials.ini
CONFIG = config.configuration()
app.secret_key = CONFIG.SECRET_KEY
FILENAME = CONFIG.DATA

#list in format of [(name, address),...]
markers = dataprocess.readIn(open(FILENAME))

##########
# pages
##

@app.route("/")
@app.route("/index")
def index():
    return flask.render_template('map.html')

@app.errorhandler(404)
def page_not_found(error):
    flask.session['linkback'] = flask.url_for("index")
    return flask.render_template('404.html'), 404

##########
# ajax request handlers that return json
##

#returns address information for map markers
@app.route("/_map_markers")
def _map_markers():
    count = request.args.get('count', type=int)
    result = {"name": markers[count - 2], "address": markers[count - 1]}
    return flask.jsonify(result=result)

#returns length of data list which contains marker information
@app.route("/_marker_count")
def _marker_count():
    result = { "count": len(markers) }
    return flask.jsonify(result=result)

##########
# other
##

app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")

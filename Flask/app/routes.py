from flask import current_app as app, json, jsonify

@app.route('/')
@app.route('/index')
def index():
    return jsonify("Index works")
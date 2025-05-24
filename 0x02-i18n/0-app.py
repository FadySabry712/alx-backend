#!/usr/bin/env python3
""" Basic Flask Implementation """
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def welcome():
    """ Wlecome Page """
    return render_tempalte('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

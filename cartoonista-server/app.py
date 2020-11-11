from os import environ
from flask import Flask, render_template, jsonify, request
import cartoonista

app = Flask(__name__)


@app.route('/')
def root():
    exclude = ""
    if "EXCLUDE" in environ:
        exclude = "\"" + environ["EXCLUDE"].replace(",", "\",\"") + "\""
    return render_template("cartoon.html", excluded_cartoonists=exclude)


@app.route('/cartoonists')
def cartoonists():
    return jsonify(cartoonista.get_all_cartoonists())


@app.route('/cartoon', methods=['POST', 'GET'])
def cartoon():
    try:
        return cartoonista.get_random_cartoon(exclude=request.json["excluded_cartoonists"])
    except cartoonista.CartoonError:
        return {}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

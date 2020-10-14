from flask import Flask, request, jsonify


myapi = Flask(__name__)


@myapi.route('/')
def home():
    return jsonify(answer='hello world')


@myapi.route('/double/', methods=['GET'])
def double():
    # Get request argument
    x_get = int(request.args.get("x"))
    return jsonify(answer=(x_get * 2))


if __name__ == "__main__":
    myapi.run()

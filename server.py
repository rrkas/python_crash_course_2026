# import flask
from flask import Flask, request

myApp = Flask("demo app")

print(__name__)


def add(a, b):
    return a + b


def concat(a, b):
    return [a, b]


@myApp.route("/ping")
def ping():
    return "pong"


@myApp.route("/add")
def handle_add():
    a = int(request.args.get("a") or "0")
    b = int(request.args.get("b") or "0")
    # return {"result": add(a, b)}
    return dict(result=add(a, b))


@myApp.route("/concat")
def handle_concat():
    a = request.args.get("a") or "0"
    b = request.args.get("b") or "0"
    # return {"result": add(a, b)}
    return dict(result=concat(a, b))



if __name__ == "__main__":
    myApp.run(debug=True, port=10000)

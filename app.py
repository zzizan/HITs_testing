from flask import Flask, request, abort
from solution import Solution

app = Flask(__name__)


@app.route("/")
def show_form():
    return "<html><head><title>Testing</title></head>" \
           "<body>" \
           "<form action='/result' method=POST>" \
           "<label for='data'>Input numbers</label><br />" \
           "<input name='data' id='data' autofocus='True'></input><br />" \
           "<input id='go' type='submit' />" \
           "</form>" \
           "</body></html>"

@app.route("/result", methods=['POST'])
def result():


    sut = Solution()
    data = request.form['data'].strip().split()

    if not all(map(lambda num: num.isdigit(), data)):
        abort(400)

    data = [int(x) for x in data]

    if len(data) > 10**4 or len(data) < 1:
        abort(400)
    for n in data:
        if n < 0 or n > 10**5:
            abort(400)

    try:
        result = str(sut.canJump(data))
    except ValueError:
        abort(400)

    return str(sut.canJump(data)), 200, {'Content-Type': 'text/plain; charset=utf-8'}
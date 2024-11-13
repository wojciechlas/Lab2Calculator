""" A simple calculator in a form of API """

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def landing_page():  # put application's code here
    """ Landing page """
    return ('<p>Welcome to Lab2Calculator!</p>'
            '<p>Use <b>/calculate</b> to calculate a pair of numbers.</p>')

@app.route('/calculate')
def calculate():  # put application's code here
    """ Calculate a pair of numbers """
    op = request.args.get('op', type=str)
    arg1 = request.args.get('arg1', type=int)
    arg2 = request.args.get('arg2', type=int)

    # addition
    if op == 'sum':
        return f'<p><b>{arg1} + {arg2} = {arg1 + arg2}</b></p>'

    # operator not recognized
    return '<p>Operation not recognized!</p>'

if __name__ == '__main__':
    app.run()

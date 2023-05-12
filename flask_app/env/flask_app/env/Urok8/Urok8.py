from flask import Flask, request, current_app, make_response, abort, g, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/books/<genre>')
def books(genre):
    res = make_response("All Books in {} category".format(genre))
    res.headers['Content-Type'] = 'text/plain'
    res.headers['Server'] = 'Foobar'
    return res

@app.route('/geturl')
def get_url():
    return redirect(url_for('books', genre='romance'))

if __name__ == "__main__":
    app.run(debug=True)
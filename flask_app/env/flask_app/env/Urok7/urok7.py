from flask import Flask, request, current_app, make_response, abort, g, render_template


app = Flask(__name__, template_folder='templates')

@app.route('/in2')
def index():
    return render_template('index2.html')

@app.route('/nav')
def index2():
    return render_template('nav.html')

if __name__ == "__main__":
    app.run(debug=True)

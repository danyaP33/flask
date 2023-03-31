from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/')
def index():
    var = 12
    template_context = dict(var=var)
    return render_template('index2.html', **template_context)


if __name__ == "__main__":
    app.run(debug=True)

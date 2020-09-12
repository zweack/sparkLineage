import os
from flask import Flask, render_template
app = Flask(__name__)

# two decorators, same function
@app.route('/')
@app.route('/index.html')
def index():
    filename = os.path.join(app.static_folder, 'data-example.json')
    return render_template('index.html', the_title='Spark Lineage', filename = filename)
@app.route('/lineage.html')
def lineage():
    filename = os.path.join(app.static_folder, 'data-example.json')
    return render_template('lineage.html', the_title='Spark Lineage', filename = filename)


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
from flask import render_template
from flask import request, redirect, url_for

from controller import crate_table, get_data, insert_data, remove_data

app = Flask(__name__)

# For docker volumes docker run --rm -p 80:80 -v $(pwd):/app {IMAGE}

@app.route('/', methods=['GET'])
def index():
    data = get_data()
    total_records = len(data)
    return render_template("index.html", data=data, total_records=total_records)


@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        name = request.form.get("name")
        phone = request.form.get("phone")
        email = request.form.get("email")
        address = request.form.get("address")
        insert_data(name, phone, email=email, address=address)
    return redirect(url_for('index'))


@app.route('/remove', methods=['POST'])
def remove():
    if request.method == 'POST':
        id = request.form.get("id")
        remove_data(id)
    return redirect(url_for('index'))


if __name__ == "__main__":
    crate_table()
    app.run(debug=True, host="0.0.0.0", port="80")

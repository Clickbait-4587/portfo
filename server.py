from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def home():
    print(url_for('static', filename='test.css'))
    return render_template('./index.html')


@app.route('/<path>')
def routes(path=None):
    return render_template(f'./{path}.html')


def write_to_csv(data):
    with open('database.csv', 'a', newline="") as db:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csvfile = csv.writer(db, delimiter=",",
                             quotechar='"', quoting=csv.QUOTE_MINIMAL)

        csvfile.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou')
        except:
            return "Did no save to database"
    else:
        return "Something went wrong! Try again..."


FLASK_APP = home
FLASK_ENV = "development"

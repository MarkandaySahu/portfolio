from flask import Flask, render_template, redirect, request
import csv

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit",methods=['GET','POST'])
def submit():
    if request.method == "POST":
        data = request.form.to_dict()
        name = data["name"]
        email = data["email"]
        message = data["message"]
        m = "Form Submitted Successfully"
        with open('db.csv', 'a', newline='') as csvfile:
            db_writer = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            db_writer.writerow([name,email,message])
        return render_template("submit.html",m=m)
    else:
        m = "Form not submitted"
        return render_template("submit.html",m=m)

#for any other page than home page
@app.route('/<string:page_name>')
def page(page_name='/'):
    try:
        return render_template(page_name)
    except:
        return redirect('/')
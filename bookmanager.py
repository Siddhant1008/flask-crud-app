import os
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

from flask_sqlalchemy import SQLAlchemy
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "attribute_database.db"))

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)

class EPC(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    AttName = db.Column(db.String(80), nullable=False)
    AttValue = db.Column(db.String(80),nullable=True)

    def __repr__(self):
        return "<Title: {},Value:{}>".format(self.AttName,self.AttValue)


@app.route('/', methods=["GET", "POST"])
def home():
    epc = None
    if request.form:
        try:
            epc = EPC(AttName=request.form.get("AttName"),AttValue=request.form.get("AttValue"))

            db.session.add(epc)
            db.session.commit()
        except Exception as e:
            print("Failed to add Attribute")
            print(e)
    epcs = EPC.query.all()
    return render_template("home.html", epcs=epcs)

@app.route("/update", methods=["POST"])
def update():
    try:
        oldAttValue = request.form.get("oldAttValue")
        newAttValue = request.form.get("newAttValue")
        AttName = request.form.get("AttName")



        epc = EPC.query.filter_by(AttValue=oldAttValue,AttName=AttName).first()
        epc.AttValue = newAttValue
        db.session.commit()
    except Exception as e:
        print("Couldn't update Attribute")
        print(e)
    return redirect("/")

@app.route("/delete", methods=["POST"])
def delete():
    AttName = request.form.get("AttName")
    epc = EPC.query.filter_by(AttName=AttName).first()
    db.session.delete(epc)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
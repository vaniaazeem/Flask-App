import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# --- App setup ---
app = Flask(__name__)

# Create instance folder (for DB)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
INSTANCE_DIR = os.path.join(BASE_DIR, "instance")
os.makedirs(INSTANCE_DIR, exist_ok=True)

# --- Database configuration ---
db_path = os.path.join(INSTANCE_DIR, "firstapp.db")
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# --- Model ---
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120))
    phone = db.Column(db.String(30))

# --- Routes ---
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        new_person = Person(
            first_name=request.form["first_name"],
            last_name=request.form["last_name"],
            email=request.form.get("email"),
            phone=request.form.get("phone")
        )
        db.session.add(new_person)
        db.session.commit()
        return redirect(url_for("home"))

    people = Person.query.all()
    return render_template("index.html", people=people)

@app.route("/delete/<int:id>")
def delete(id):
    person = Person.query.get_or_404(id)
    db.session.delete(person)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    person = Person.query.get_or_404(id)
    if request.method == "POST":
        person.first_name = request.form["first_name"]
        person.last_name = request.form["last_name"]
        person.email = request.form["email"]
        person.phone = request.form["phone"]
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("update.html", person=person)

# --- Run app ---
if __name__ == "__main__":
    with app.app_context():
        if not os.path.exists(db_path):
            db.create_all()
            print("✅ Database created at:", db_path)
        else:
            print("📂 Using existing database:", db_path)
    app.run(debug=True)

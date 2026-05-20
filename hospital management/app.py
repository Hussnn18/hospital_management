from flask import Flask, render_template, request, redirect, url_for
from db import get_connection

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("dashboard.html")


@app.route("/patients", methods=["GET", "POST"])
def patients():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)

    if request.method == "POST":
        name = request.form['name']
        age = request.form['age']
        cur.execute("INSERT INTO patient (Name, Age) VALUES (%s, %s)", (name, age))
        conn.commit()

    cur.execute("SELECT * FROM patient")
    data = cur.fetchall()
    conn.close()
    return render_template("patient.html", patients=data)


@app.route("/delete_patient/<int:id>")
def delete_patient(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM patient WHERE patient_id=%s", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('patients'))


@app.route("/doctors", methods=["GET", "POST"])
def doctors():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)

    if request.method == "POST":
        name = request.form['name']
        specialization = request.form['specialization']
        cur.execute(
            "INSERT INTO doctor (Name, Specialization) VALUES (%s, %s)",
            (name, specialization)
        )
        conn.commit()

    cur.execute("SELECT * FROM doctor")
    data = cur.fetchall()
    conn.close()
    return render_template("doctor.html", doctors=data)


@app.route("/delete_doctor/<int:id>")
def delete_doctor(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM doctor WHERE doctor_id=%s", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('doctors'))


@app.route("/appointments", methods=["GET", "POST"])
def appointments():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)

    if request.method == "POST":
        date = request.form['appointment_date']
        disease = request.form['disease']
        patient_id = request.form['patient_id']
        doctor_id = request.form['doctor_id']

        cur.execute(
            "INSERT INTO appointment (appointment_date, disease, patient_id, doctor_id) VALUES (%s, %s, %s, %s)",
            (date, disease, patient_id, doctor_id)
        )
        conn.commit()

    cur.execute("""
        SELECT a.appointment_id, a.appointment_date, a.disease,
               p.Name AS patient_name, d.Name AS doctor_name
        FROM appointment a
        JOIN patient p ON a.patient_id = p.patient_id
        JOIN doctor d ON a.doctor_id = d.doctor_id
    """)
    data = cur.fetchall()
    conn.close()
    return render_template("appointment.html", appointments=data)


@app.route("/delete_appointment/<int:id>")
def delete_appointment(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM appointment WHERE appointment_id=%s", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('appointments'))


@app.route("/treatments", methods=["GET", "POST"])
def treatments():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)

    if request.method == "POST":
        desc = request.form['description']
        med = request.form['medicine']
        appointment_id = request.form['appointment_id']

        cur.execute(
            "INSERT INTO treatment (description, medicine, appointment_id) VALUES (%s, %s, %s)",
            (desc, med, appointment_id)
        )
        conn.commit()

    cur.execute("""
        SELECT t.treatment_id, t.description, t.medicine,
               a.appointment_id
        FROM treatment t
        JOIN appointment a ON t.appointment_id = a.appointment_id
    """)
    data = cur.fetchall()
    conn.close()
    return render_template("treatment.html", treatments=data)


@app.route("/delete_treatment/<int:id>")
def delete_treatment(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM treatment WHERE treatment_id=%s", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('treatments'))


@app.route("/bills", methods=["GET", "POST"])
def bills():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)

    if request.method == "POST":
        bill_id = request.form['bill_id']
        amount = request.form['amount']
        bill_date = request.form['bill_date']
        patient_id = request.form['patient_id']

        cur.execute(
            "INSERT INTO bill (bill_id, amount, bill_date, patient_id) VALUES (%s, %s, %s, %s)",
            (bill_id, amount, bill_date, patient_id)
        )
        conn.commit()

    cur.execute("""
        SELECT b.bill_id, b.amount, b.bill_date, p.Name AS patient
        FROM bill b
        JOIN patient p ON b.patient_id = p.patient_id
    """)
    data = cur.fetchall()
    conn.close()
    return render_template("bill.html", bills=data)


@app.route("/delete_bill/<int:id>")
def delete_bill(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM bill WHERE bill_id=%s", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('bills'))


if __name__ == "__main__":
    app.run(debug=True)
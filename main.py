from flask import Flask, render_template
import psycopg2

app = Flask('')

@app.route('/records')
def records():
    con = psycopg2.connect(user="indmfojfvoiiem",
                           password="facdfb9fe6e90a07401ae02ef4e2297fa93c2bf6d205648e5d7e062c0c8da8bb",
                           host="ec2-54-247-78-30.eu-west-1.compute.amazonaws.com",
                           port="5432",
                           database="dd2pdbo5s56kui")
    cur = con.cursor()
    cur.execute("SELECT * FROM u;")
    persons = cur.fetchall()
    con.commit()
    con.close()
    persons = sorted(persons, key=lambda x: -x[-1])
    return render_template('records.html', title='Рекорды', persons=persons)


def run():
    app.run(host="127.0.0.1", port=8080)

run()
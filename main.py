from flask import Flask, render_template, jsonify
import pymysql

app = Flask(__name__)

# Put in information to the db converted from R to SQL
db = pymysql.connect(
    host='db_host',
    user='username',
    password='password',
    database='db_name'
)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/get_player_metrics')
def get_player_metrics():
    cursor = db.cursor()

    cursor.execute("SELECT player_name, score FROM player_metrics")
    data = cursor.fetchall()

    labels = [row[0] for row in data]
    scores = [row[1] for row in data]

    return jsonify({'labels': labels, 'scores': scores})

if __name__ == '__main__':
    app.run(debug=True)
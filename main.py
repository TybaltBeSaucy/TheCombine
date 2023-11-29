from flask import Flask, render_template, jsonify
import pymysql
from over_under_check import over_under_check

app = Flask(__name__)

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

    home_team_to_check = 'Arizona Cardinals'
    your_single_number = 50

    over_under_data = over_under_check(home_team_to_check, your_single_number)

    merged_data = [{'Player': row[0], 'Score': row[1], 'Percentage': over_under_data.get(row[0], 0)} for row in data]

    return jsonify(merged_data)

if __name__ == '__main__':
    app.run(debug=True)

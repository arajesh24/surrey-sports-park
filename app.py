from flask import Flask, render_template, jsonify , redirect
import pymysql
import os

app = Flask(__name__)

# MySQL Configuration
#DB_HOST = os.environ.get('DB_HOST')
#DB_USER = os.environ.get('DB_USER')
#DB_PASS = os.environ.get('DB_PASS')
#DB_NAME = os.environ.get('DB_NAME')
#JWT_SECRET = os.environ.get('JWT_SECRET')
#PORT = os.environ.get('PORT', 3000)

#def query_database(query):
#    conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME)
#    cursor = conn.cursor(pymysql.cursors.DictCursor)
#    cursor.execute(query)
#    results = cursor.fetchall()
#    cursor.close()
#    conn.close()
#    return results

# Route for the home page
#@app.route('/home')
#def home():

#    current_query = "SELECT * FROM bookings WHERE date >= CURDATE()"
#    past_query = "SELECT * FROM bookings WHERE date < CURDATE()"
    
#    current_bookings = query_database(current_query)
#    past_bookings = query_database(past_query)
    
#    return render_template('home.html', current_bookings=current_bookings, past_bookings=past_bookings)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')
# Route for the about-us page
@app.route('/about-us')
def about_us():
    return render_template('about-us.html')

# Route for the sports page
@app.route('/sports')
def sports():
    return render_template('sports.html')

# Route for the football page
@app.route('/football')
def football():
    return render_template('football.html')

# Route for the badminton page
@app.route('/badminton')
def badminton():
    return render_template('badminton.html')

# Route for the cricket page
@app.route('/cricket')
def cricket():
    return render_template('cricket.html')
# Route for the my-bookings page
#@app.route('/booking')
#def booking():
#    return redirect('/<bookingurl>')



if __name__ == '__main__':
    app.run(debug=True)


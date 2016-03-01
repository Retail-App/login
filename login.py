__author__ = '8422'
from flask import Flask, jsonify,request
import MySQLdb
import json
app = Flask(__name__)

db = MySQLdb.connect(host = "localhost",
                        user = "sanjana",
                        passwd = "root",
                        db = "infinity")
cur = db.cursor()

@app.route('/',methods=['post'])
def index():
    print request.data
    request_data = json.loads(request.data)
    dict1 = {}

    sql = "SELECT password from user WHERE email= %s"
    data = (request_data['email'].encode('utf-8'),)
    cur.execute(sql,data)
    passw = cur.fetchone()
    passw = passw[0]
    if request_data['pass'].encode('utf-8') == passw:
        dict1['message'] = "successful"
        dict1['status'] = 1
    else:
        dict1['message'] = "fail"
        dict1['status'] = 0


    print request_data
    return jsonify(dict1)

@app.route('/login')
def index1():
    return "Hello, World test!"

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)
    #app.run(debug=True)

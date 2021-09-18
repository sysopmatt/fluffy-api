import sqlite3
import confuse
from flask import Flask, request, jsonify
import os

config = confuse.Configuration('fluffy-api', __name__)

connection = sqlite3.connect('fluffy.db')
ApiKeys = list()

cursor = connection.cursor()
cursor.execute("SELECT DISTINCT ApiKey FROM FluffyUsers;")
row = cursor.fetchall()
for key in row:
    ApiKeys.append(key[0])
cursor.close()

app = Flask(__name__)


@app.route('/Upload/', methods=['POST'])
def index():
    headers = request.headers
    auth = headers.get("X-Api-Key")
    if auth in ApiKeys:
        return jsonify({"message": "OK: Authorized"}), 200
    else:
        return jsonify({"message": "ERROR: Unauthorized"}), 401


if __name__ == '__main__':
    app.run(port = int(os.environ.get('PORT', 5000)))

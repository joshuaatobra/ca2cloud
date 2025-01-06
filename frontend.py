import os
from flask import Flask, request, jsonify

app = Flask(__name__)


api_key = os.getenv('ApiKey')

@app.route('/')
def form():
    return f'''
        <html>
            <body>
                <h2>Enter Your Details</h2>
                <form method="POST" action="/submit">
                    Name: <input type="text" name="name"><br><br>
                    Email: <input type="email" name="email"><br><br>
                    <input type="submit" value="Submit">
                </form>
                <p><strong>API Key:</strong> {api_key if api_key else "Not Configured"}</p>
            </body>
        </html>
    '''

@app.route('/submit', methods=["POST"])
def submit():
    name = request.form['name']
    email = request.form['email']
    return jsonify({"name": name, "email": email, "api_key": api_key})

if __name__ == '__main__':
    app.run(debug=True)



from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def form():
    return '''
        <html>
            <body>
                <h2>Enter Your Details</h2>
                <form method="POST" action="/submit">
                    Name: <input type="text" name="name"><br><br>
                    Email: <input type="email" name="email"><br><br>
                    <input type="submit" value="Submit">
                </form>
            </body>
        </html>
    '''

@app.route('/submit', methods=["POST"])
def submit():
    name = request.form['name']
    email = request.form['email']
    return jsonify({"name": name, "email": email})

if __name__ == '__main__':
    app.run(debug=True)

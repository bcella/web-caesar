from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <!DOCTYPE html>
    <html>
        <head>
            <style>
                form {
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }
                textarea {
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }
            </style>
        </head>
        <body>
            <form method="POST">
                <label for="rot">Rotate by:</label>
                <input type="text" name="rot" value="0">
                <input type="textarea" name="text">
                <input type="submit">
            </form>
        </body>
    </html>
"""

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    rotation = request.form['rot']
    rotation_int = int(rotation)
    message = request.form['text']
    encrypt_message = rotate_string(message, rotation_int)

    return "<h1>" + encrypt_message + "</h1>"


app.run()
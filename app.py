from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return """<html>
                <head><title>Flask App</title></head>
                <body>
                    <h1>Welcome to the Flask App!
                        <br>From Tanishq Singh
                        <br>From Batch 2
                    </h1>
                </body>
              </html>"""

@app.route('/hello/', methods=['GET'])
def create():
    return """<html>
                <head><title>Hello Page</title></head>
                <body>
                    <h1>Hello, World!</h1>
                </body>
              </html>"""

@app.route('/datetime/', methods=['GET'])
def get_datetime():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""<html>
                <head><title>DateTime Page</title></head>
                <body>
                    <h1>Current Date and Time: {current_time}</h1>
                </body>
               </html>"""

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
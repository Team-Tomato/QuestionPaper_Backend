from flask import Flask, jsonify
app=Flask(__name__)
movies = [
    {
        "name":"kaithi",
        "casts":["karthick","Arjun Das"],
        "genres":["action"]
    },
    {
        "name":"VTV",
        "casts":["str","trisha"],
        "genres":["romance"]
    }
]
@app.route('/movies')
def hello():
    return jsonify(movies)
app.run()

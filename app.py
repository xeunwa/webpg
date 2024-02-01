from flask import Flask, render_template, Response

app = Flask(__name__)
FLAG = open("flag.txt", "r").read()

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route("/flag", methods=["GET"])
def flag():
    return Response(FLAG, mimetype="text/plain")

if __name__ == '__main__':
    app.run(debug=False, port=5000, host='0.0.0.0')

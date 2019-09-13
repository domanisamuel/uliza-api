from flask import Flask
app = Flask(__name__)

@app.route('/')
def uliza():
    return "welcome to uliza"

if __name__  ==   "__main__":
    app.run()
from flask import Flask, render_templete

app = Flask(__name__)

@app.route('/')
def index():
    return render_templete('index.html')

if __name__ == '__main__':
    app.run( )
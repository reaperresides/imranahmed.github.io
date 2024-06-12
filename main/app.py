from flask import Flask, render_template,send_file
from flask_bootstrap import Bootstrap
import os

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/download')
def download_file():
    file_path = 'static/files/resume.pdf'
    return send_file(file_path, as_attachment=True)

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,port=port,host="0.0.0.0")

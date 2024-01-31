from flask import Flask, render_template

app = Flask (__name__)


@app.route ('/')
def home():
    return render_template ('home.html')


@app.route ('/Docs')
def docs():
    return render_template ('Docs.html')


@app.route ('/Hilbert_Space_Study')
def hilbert_space_study():
    return render_template ('Hilbert_Space_Study.html')


if __name__ == '__main__':
    app.run (debug=True)

from flask import Flask, render_template, jsonify
import Quantum_Algorithm_Suite  # Corrected module name

app = Flask (__name__)


@app.route ('/')
def home():
    return render_template ('home.html')


@app.route ('/sass')
def sass():
    return render_template ('sass.html')


@app.route ('/badges')
def badges():
    return render_template ('badges.html')


@app.route ('/collapsible')
def collapsible():
    return render_template ('collapsible.html')


@app.route ('/api/data')
def get_data():
    data = Quantum_Algorithm_Suite.quantum_algorithm_suite (50, 0.5, 1)  # Corrected function name
    return jsonify (data)


if __name__ == '__main__':
    app.run (debug=True)

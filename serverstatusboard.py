from flask import Flask, request, redirect, url_for, jsonify
app = Flask(__name__)


@app.route('/')
def root():
    return redirect(url_for('static', filename='index.html'))


@app.route('/status/<int:num>', methods=['GET'])
def get_status(num):
    return jsonify({'working_status': free})

@app.route('/set_status/<int:num>', methods=['POST'])
def set_status(num):
    if (request.method == 'POST'):
        some_json = request.get_json()
        return jsonify({'set_status': some_json}), 201

if __name__ == '__main__':
    app.run(debug=True)

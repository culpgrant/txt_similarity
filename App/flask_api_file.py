""""
This is the file that has the flask API for the function in text_similarity.py
"""

import flask
from text_similarity import determine_txt_similarity


# Creating the Flask Object
app = flask.Flask(__name__)
app.config['DEBUG'] = True


# Routing to the main page
@app.route('/', methods=['GET'])
def home():
    return "<h1>Text Similarity API</h1>"


# Route to return all of the entries
@app.route('/api/v1/get_txt_similarity', methods=['POST'])
def api_return_txt_similarity():
    # Getting the data from the request
    txt_one = flask.request.json.get('txt_one', '')
    txt_two = flask.request.json.get('txt_two', '')
    result = round(determine_txt_similarity(txt_one, txt_two), 2)
    # Preparing the return result
    return_result = {
        'txt_one': txt_one,
        'txt_two': txt_two,
        'similarity_score': result
    }
    return flask.jsonify(return_result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

from flask import Flask, request, render_template
from tensorflow.keras.models import load_model

import input_preprocess
import similar_pgm

app = Flask(__name__)


@app.route('/')  # 라우팅
def home():
    return render_template('index.html')


@app.route('/aboutFH')
def aboutFH():
    return render_template('aboutFH.html')


@app.route('/aboutUS')
def aboutUS():
    return render_template('aboutUS.html')


@app.route('/', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':

        total_input = [x for x in request.form.values()]

        X1_input = input_preprocess.make_X1input(total_input[1:4])
        X2_input = input_preprocess.make_X2input(total_input[4:7])
        X3_input = input_preprocess.make_X3input(total_input[7])

        sentence_model = load_model("01_sentence.h5")
        probation_model = load_model('02_probation.h5')
        y_sentence = sentence_model.predict([X1_input, X2_input, X3_input])
        y_probation = probation_model.predict([X1_input, X2_input, X3_input])
        sim_url, sim_title = similar_pgm.find_similar_pgm(total_input[7])

        if total_input[0] == '네':
            appeal_model = load_model('03_appeal.h5')
            y_appeal = appeal_model.predict([X1_input, X2_input, X3_input])
            return render_template('result_2.html', y_sentence=round(y_sentence, 2), y_probation=round(y_probation[0][1], 2), y_appeal=round(y_appeal[0][1], 2), sim_url=sim_url, sim_title=sim_title)
        else:
            return render_template('result_1.html', y_sentence=round(y_sentence, 2), y_probation=round(y_probation[0][1], 2), sim_url=sim_url, sim_title=sim_title)

if __name__ == "__main__":
    app.run(debug=True)

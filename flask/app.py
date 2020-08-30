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
        print(total_input)

        X1_input = input_preprocess.make_X1input(total_input[1:4])
        X2_input = input_preprocess.make_X2input(total_input[4:7])
        X3_input = input_preprocess.make_X3input(total_input[7])

        sentence_model = load_model("01_sentence.h5")
        probation_model = load_model('02_probation.h5')
        y_sentence = sentence_model.predict([X1_input, X2_input, X3_input])
        y_pobation = probation_model.predict([X1_input, X2_input, X3_input])
        sim_url = similar_pgm.find_similar_pgm(total_input[7])

        if total_input[0] == '네':
            appeal_model = load_model('03_appeal.h5')
            y_appeal = appeal_model.predict([X1_input, X2_input, X3_input])
            return render_template('result.html', y_sentence=y_sentence, y_pobation=y_pobation, y_appeal=y_appeal, sim_url=sim_url)
        else:
            return render_template('result.html', y_sentence=y_sentence, y_pobation=y_pobation, sim_url=sim_url)

if __name__ == "__main__":
    app.run(debug=True)

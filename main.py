from flask import Flask, render_template, request
from translate import translate
from classify import classify_query

app = Flask(__name__,static_url_path='', static_folder='web/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/NyaaySahaayak')
def NyaaySahaayak():
    return render_template('NyaaySahaayak.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['user_message']
    classification = classify_query(user_message)
    if classification == 'Non-Indian Legal':
        response = "Apologies, but I'm here to assist with questions related to Indian laws and legal matters only. If you have any queries within this domain, feel free to ask. Otherwise, I may not have the information you're looking for. Thank you for understanding."
    else:
        response = translate(user_message)
    return {'bot_response': response}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860)

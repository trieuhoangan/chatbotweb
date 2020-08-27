from flask import Flask, Response,request, send_from_directory, render_template
import requests

app = Flask(__name__,static_url_path='/static')
app.config.from_object(__name__)
utter_intent = ['greeting','end_conversation','ask_point','ask_faculty']
utter_response = ['chào bạn, bạn muốn hỏi gì về trường đại học công nghệ','tạm biệt','25','cntt']
response_intent = ['ask_information']
@app.route('/')
def root():
    message = "chatbotUET"
    return render_template('index.html', message=message)
@app.route('/get_response',methods=['POST'])
def get_response():
    response_text = request.get_data(as_text=True)
    rasa_url = "http://localhost:5005/model/parse"
    r = requests.post(rasa_url,data=str(response_text).encode('utf-8'))
    data = r.json()
    print(data)
    intent = data['intent']['name']
    print(intent)
    if intent in utter_intent:
        return {'text':utter_response[utter_intent.index(intent)]}
    else:
        return data['response_selector']['default']['response']['name']
    
if __name__ == "__main__":
    app.run(host= '0.0.0.0',port=3000)
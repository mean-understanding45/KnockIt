from flask import Flask,jsonify,request
import requests,json
from openai import OpenAI
app = Flask(__name__)

client = OpenAI(api_key="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")

@app.route('/')
def hello():
    return "Ready to Go!!!!"


@app.route('/getResponse',methods=['POST'])
def getGPTResponse():
    data = request.get_json()

    return requestGPT("Hi"))


def requestGPT(prompt):
    messages=[{"role": "user", "content": prompt}]
    model="gpt-3.5-turbo-1106"
    response = client.chat.completions.create(model=model,messages=messages)
    print(response)
    return response.choices[0].message.content.strip()

if __name__ == '__main__':
    app.run(debug=True)


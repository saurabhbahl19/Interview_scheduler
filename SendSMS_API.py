import nexmo
from flask import Flask,request, json, render_template
from flask_cors import CORS

app = Flask(__name__)
client = nexmo.Client(key='a2450d0c', secret='6msFdAEGHyj4niVh')
cors = CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sendSMS/api/v1.0/send_sms', methods=['POST'])
def sendSmsAPI():
  if request.headers['Content-Type'] == 'application/json':
       data = json.loads(request.data)
       listOfPhoneNumbers = data["phoneNumbers"]
       message = data["message"]
       for eachPhoneNumber in listOfPhoneNumbers:
           sendSMSService(eachPhoneNumber,message)
       return "SMS SENT TO ALL THE PHONE NUMBERS"    
      
  else:
    return "415 Unsupported Media Type ;)" 

def sendSMSService(phoneNumbers, message):
    client.send_message({'from': '12015152281', 'to': phoneNumbers, 'text': message})




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80,debug=True)

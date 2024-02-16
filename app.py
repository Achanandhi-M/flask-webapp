import pdb
import requests
from flask import Flask, request,jsonify,redirect,url_for
app=Flask(__name__)

@app.route('/',methods=['POST'])
def upload():
    data=request.json
    file_name=data.get('file')
    url = 'https://app.nanonets.com/api/v2/OCR/Model/b0346511-e554-4595-bc57-e30363020fc1/LabelFile/?async=false'
    data = {'file': open(file_name, 'rb')}
    response = requests.post(url, auth=requests.auth.HTTPBasicAuth(
    '081ff6c2-b5e1-11ee-a4d4-8ed5ab0bd968', ''), files=data)
    if response.status_code == 200:
        present_meter_value= (response.json()['result'][0]['prediction'][0]['ocr_text'].split('CUM ')[-1].split('kw h')[0])
        si_no= (response.json()['result'][0]['prediction'][0]['ocr_text'].split('Month / Year\nMO\n')[-1].split(' ')[0])
        if si_no== '00479560':
            response_data = {
               "meter_value": present_meter_value
            }
            return jsonify(response_data),200
        else:
            return jsonify({"error": "Invalid SI number"}),404
        
    return jsonify({error:"Failed to process the request"}), 500


@app.route('/calculate',methods=['POST'])

def calculate():

    previous_meter_value=2000
    meter_data=request.json
    present_meter_value=meter_data.get('present_meter_value')
    present_meter_value = float(present_meter_value)
    total_units_consumed=present_meter_value-previous_meter_value
    print(total_units_consumed)
    total_amount=total_units_consumed*20
    print(total_amount)
    calculated_amount={
        "total unit consumed is": total_units_consumed,
        "total amount is": total_amount
    }
    return jsonify(calculated_amount),200


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "YOUR_API_KEY"
API_URL = "https://api.freecurrencyapi.com/v1/latest"

@app.route('/', methods=['GET','POST'])
def index():
    result = None
    currencies = []

    response = requests.get(f"{API_URL}?apikey={API_KEY}")
    if response.status_code == 200:
        data = response.json()
        currencies = list(data["data"].keys())
    else:
        return "Error to fetchhing data from API"
    
    if request.method == 'POST':
        from_currency = request.form.get('from_currency')
        to_currency = request.form.get('to_currency')
        amount = float(request.form.get('amount'))

        rates = data["data"]
        if from_currency in rates and to_currency in rates:
            from_rate = float(rates[from_currency])
            to_rate = float(rates[to_currency])
            conversion_result = amount * (to_rate / from_rate)
            result = {
                "amount" : round(conversion_result, 2),
                "to_currency" : to_currency
            }
        else:
            result = "Conversion error"

    return render_template('index.html', currencies=currencies, result=result)

if __name__ == '__main__':
    app.run(debug=True)
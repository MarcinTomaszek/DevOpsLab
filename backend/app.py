from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/api/rates")
def get_rates():
    url = "https://api.exchangerate.host/latest?base=USD&symbols=EUR,GBP,CHF,PLN"
    response = requests.get(url).json()

    return jsonify({
        "base": response["base"],
        "rates": response["rates"],
        "date": response["date"]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

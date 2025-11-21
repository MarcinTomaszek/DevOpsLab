from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/api/rates")
def get_rates():
    url = "https://api.exchangerate.host/latest?base=USD&symbols=EUR,GBP,CHF,PLN"
    response = requests.get(url).json()

    # Logowanie odpowiedzi API
    print("API RESPONSE:", response)

    # API zwróciło error?
    if not response.get("success", True):
        return jsonify({
            "error": response.get("error", "Unexpected API error"),
            "raw_response": response
        }), 500

    # Bezpiecznie pobieramy wartości
    base = response.get("base", "USD")
    rates = response.get("rates", {})
    date = response.get("date", "")

    return jsonify({
        "base": base,
        "rates": rates,
        "date": date
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

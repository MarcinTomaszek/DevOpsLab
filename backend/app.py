from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/api/rates")
def get_rates():
    # API Frankfurter – base USD, target currencies
    url = "https://api.frankfurter.app/latest?from=USD&to=EUR,GBP,CHF,PLN"
    try:
        response = requests.get(url, timeout=5).json()
    except Exception as e:
        return jsonify({"error": "Błąd połączenia z API", "details": str(e)}), 500

    rates = response.get("rates")
    if not rates:
        return jsonify({"error": "Brak danych rates", "raw_response": response}), 500

    return jsonify({
        "base": response.get("base", "USD"),
        "rates": rates,
        "date": response.get("date", "")
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/api/rates")
def get_rates():
    url = "https://api.frankfurter.app/latest?from=USD&to=EUR,GBP,CHF,PLN"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()  # <-- upewnij się, że JSON jest poprawnie parsowany

        return jsonify({
            "base": data.get("base"),
            "date": data.get("date"),
            "rates": data.get("rates")
        })
    except Exception as e:
        return jsonify({"error": "Błąd połączenia z API", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

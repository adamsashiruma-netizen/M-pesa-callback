from flask import Flask, request

app = Flask(__name__)

@app.route("/callback", methods=["POST"])
def callback():
    data = request.json
    print("M-PESA CALLBACK:")
    print(data)
    return {"ResultCode": 0, "ResultDesc": "Accepted"}

@app.route("/")
def home():
    return "M-PESA callback server is running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

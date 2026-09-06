from flask import Flask, render_template

app = Flask(__name__)

WHATSAPP = "https://wa.me/2349125747577"

@app.route("/")
def home():
    return render_template(
        "index.html",
        whatsapp=WHATSAPP
    )

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )

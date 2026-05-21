from urllib import response

from flask import Flask, render_template, request, jsonify
from google import genai

app = Flask(__name__)

# PASTE YOUR API KEY HERE
client = genai.Client(api_key="AIzaSyDt1xNOu7xKEqvocjNbJAGS6k3hK2bOHJY")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/strategy", methods=["POST"])
def strategy():

    data = request.json

    track = data["track"]
    lap = data["lap"]
    tire = data["tire"]
    wear = data["wear"]
    weather = data["weather"]
    fuel = data["fuel"]

    prompt = f"""
    You are an elite Formula 1 race engineer.

    Analyze the following telemetry:

    Track: {track}
    Current Lap: {lap}
    Tire Compound: {tire}
    Tire Wear: {wear}%
    Weather: {weather}
    Fuel Level: {fuel}%

    Give:
    - Pit strategy
    - Tire recommendation
    - Fuel management advice
    - Driving push/conserve recommendation

    Speak like a real F1 race engineer.
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        ai_response = response.text
    except Exception as e:
        ai_response = f"""
    AI service temporarily unavailable.

    Fallback Strategy:

    Tire degradation is increasing rapidly.
    Pit within the next 2 laps.
    Switch to Medium compound.
    Fuel levels support aggressive pace.
    Weather conditions should be monitored carefully.
    """

    return jsonify({
        "response": ai_response
    })

if __name__ == "__main__":
    app.run(debug=True)
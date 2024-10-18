"""
Flask application for emotion detection based on user input text.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("EmotionDetector")

@app.route("/emotionDetector")
def sent_detector():
    """
    Analyze the provided text for emotions and return the results.

    Returns:
        str: A message indicating the emotion results or an error message for invalid input.
    """
    text_to_analyze = request.args.get("textToAnalyze", "").strip()

    # Check for blank input
    if not text_to_analyze:
        return "Invalid input, please provide some text to analyze."

    response = emotion_detector(text_to_analyze)
    print(response)

    # Extract emotions from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid input, please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy}, and 'sadness': {sadness}. The dominant "
        f"emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Render the index HTML page.

    Returns:
        str: The rendered index.html page.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, request, render_template

from EmotionDetection import emotion_detector

app = Flask('EmotionDetector')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detector_route():
    text_to_analyze = request.args.get('textToAnalyze')    
    result = emotion_detector(text_to_analyze)
    scores_text = f"'anger': {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} and 'sadness': {result['sadness']}"
    dominant_emotion = result['dominant_emotion']
    response = f"For the given statement, the system response is {scores_text}. The dominant emotion is {dominant_emotion}"
    return response

if __name__ == '__main__':
    app.run()
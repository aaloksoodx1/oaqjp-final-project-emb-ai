import requests
import json

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}


def emotion_detector(text_to_analyze):
    input_json = { "raw_document": { "text": text_to_analyze } }
    resp = requests.post(url=URL, json=input_json, headers=HEADERS)
    result = json.loads(resp.text)
    emotion_scores = result["emotionPredictions"][0]['emotion']
    max_score = -1
    dominant_emotion = None
    for emotion, score in emotion_scores.items():
        if score > max_score:
            dominant_emotion = emotion
            max_score = score
    
    emotion_scores['dominant_emotion'] = dominant_emotion
    return emotion_scores



import requests
import json
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers = header)
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        dominant_score = 0
        dominant_emotion = None
        for emotion in emotions:
            if emotions[emotion] > dominant_score:
                dominant_score = emotions[emotion]
                dominant_emotion = emotion
        emotions['dominant_emotion'] = dominant_emotion
        return emotions
    else:
        return {'anger': None, \
                'disgust': None, \
                'fear': None, \
                'joy': None, \
                'sadness': None, \
                'dominant_emotion': None}
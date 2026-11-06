"""Task 3 snapshot: format Watson emotion scores and select the maximum."""

import json

import requests

API_URL = (
    "https://sn-watson-emotion.labs.skills.network/v1/"
    "watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}
EMOTIONS = ("anger", "disgust", "fear", "joy", "sadness")


def emotion_detector(text_to_analyze):
    """Return the five emotion scores plus the dominant emotion."""
    response = requests.post(
        API_URL,
        headers=HEADERS,
        json={"raw_document": {"text": text_to_analyze}},
        timeout=30,
    )
    response.raise_for_status()
    response_dict = json.loads(response.text)
    scores = response_dict["emotionPredictions"][0]["emotion"]
    result = {emotion: scores[emotion] for emotion in EMOTIONS}
    result["dominant_emotion"] = max(result, key=result.get)
    return result

"""Detect five emotions using the Skills Network Watson NLP service."""

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
    """Return emotion scores and their maximum, or None values for invalid text."""
    empty_result = dict.fromkeys((*EMOTIONS, "dominant_emotion"))
    if not isinstance(text_to_analyze, str) or not text_to_analyze.strip():
        return empty_result

    response = requests.post(
        API_URL,
        headers=HEADERS,
        json={"raw_document": {"text": text_to_analyze}},
        timeout=30,
    )
    if response.status_code == 400:
        return empty_result
    response.raise_for_status()
    response_dict = json.loads(response.text)
    scores = response_dict["emotionPredictions"][0]["emotion"]
    result = {emotion: scores[emotion] for emotion in EMOTIONS}
    result["dominant_emotion"] = max(result, key=result.get)
    return result

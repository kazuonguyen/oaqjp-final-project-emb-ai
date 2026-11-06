"""Task 2 snapshot: return the raw response text before formatting."""

import requests


def emotion_detector(text_to_analyze):
    """Call Watson EmotionPredict and return its response text."""
    url = (
        "https://sn-watson-emotion.labs.skills.network/v1/"
        "watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    response = requests.post(
        url,
        json={"raw_document": {"text": text_to_analyze}},
        headers=headers,
        timeout=30,
    )
    response.raise_for_status()
    return response.text

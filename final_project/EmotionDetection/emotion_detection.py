import requests 

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input = { "raw_document": { "text": text_to_analyse } }
    res = requests.post(url, headers=header, json=input)
    if res.status_code == 400:
        return {
            "anger": None, 
            "disgust": None, 
            "fear": None, 
            "joy": None, 
            "sadness": None, 
            "dominant_emotion":None
            }
    elif res.status_code == 200:
        res_out = res.json()
        res_modified = res_out['emotionPredictions'][0]['emotion']
        dom_em=''
        score=0
        for em in res_modified:
            score_new = res_modified[em]
            if score_new>score: 
                dom_em = em
                score = score_new
        res_modified['dominant_emotion'] = dom_em
        return res_modified
        
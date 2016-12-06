import http.client
import sys
import json
import math


def get_emotion(file_path, header):
    try:
        conn = http.client.HTTPSConnection('api.projectoxford.ai')
        conn.request("POST", "/emotion/v1.0/recognize?", open(file_path, 'rb'), header)
        response = conn.getresponse()
        response_data = response.read()
        json_data = json.loads(response_data.decode('utf-8'))
        conn.close()
        return json_data

    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
        print(e.message)


def float_format(num):
    return '%.6f' % num


def my_round(num, d=0):
    p = 10 ** d
    return float(math.floor((num * p) + math.copysign(0.5, num))) / p


if __name__ == '__main__':

    with open('api_key.txt', 'r') as f:
        api_key = f.read().rstrip('\n')

    headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': api_key,
    }

    data = get_emotion(sys.argv[1], headers)
    print(data)

    for face in data:
        face_rectangle = face['faceRectangle']
        face_scores = face['scores']
        face_surprise = float_format(face_scores['surprise'])
        face_contempt = float_format(face_scores['contempt'])
        face_disgust = float_format(face_scores['disgust'])
        face_fear = float_format(face_scores['fear'])
        face_neutral = float_format(face_scores['neutral'])
        face_anger = float_format(face_scores['anger'])
        face_happiness = float_format(my_round(face_scores['happiness'], 6))
        face_sadness = float_format(face_scores['sadness'])
        print('Surprise: ', face_surprise)
        print('Contempt: ', face_contempt)
        print('Disgust: ', face_disgust)
        print('Fear: ', face_fear)
        print('Neutral: ', face_neutral)
        print('Anger: ', face_anger)
        print('Happiness: ', face_happiness)
        print('Sadness: ', face_sadness)

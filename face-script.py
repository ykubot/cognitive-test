import http.client
import sys
import json
import math
import urllib


def get_faceinfo(file_path, param, header):
    try:
        conn = http.client.HTTPSConnection('api.projectoxford.ai')
        conn.request("POST", "/face/v1.0/detect?%s" % param, open(file_path, 'rb'), header)
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

    with open('api_key_face.txt', 'r') as f:
        api_key = f.read().rstrip('\n')

    headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': api_key,
    }

    params = urllib.parse.urlencode({
        # Request parameters
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender,glasses,facialHair,headPose'
    })

    data = get_faceinfo(sys.argv[1], params, headers)
    print(data)

    # for face in data:
    #     face_rectangle = face['faceRectangle']
    #     face_scores = face['scores']
    #     face_surprise = float_format(face_scores['surprise'])
    #     face_contempt = float_format(face_scores['contempt'])
    #     face_disgust = float_format(face_scores['disgust'])
    #     face_fear = float_format(face_scores['fear'])
    #     face_neutral = float_format(face_scores['neutral'])
    #     face_anger = float_format(face_scores['anger'])
    #     face_happiness = float_format(my_round(face_scores['happiness'], 6))
    #     face_sadness = float_format(face_scores['sadness'])
    #     print('Surprise: ', face_surprise)
    #     print('Contempt: ', face_contempt)
    #     print('Disgust: ', face_disgust)
    #     print('Fear: ', face_fear)
    #     print('Neutral: ', face_neutral)
    #     print('Anger: ', face_anger)
    #     print('Happiness: ', face_happiness)
    #     print('Sadness: ', face_sadness)




# Face Attributes:
# age: an age number in years.
# gender: male or female.
# smile: smile intensity, a number between[0, 1]
# facialHair: consists of lengths of three facial hair
# areas: moustache, beard and sideburns.
# headPose: 3 - D roll / yew / pitch angles for face direction.Pitch value is a reserved field and will always return 0.
# glasses: glasses type.Possible values are 'noGlasses', 'readingGlasses', 'sunglasses', 'swimmingGoggles'.

# Response json
# [
#     {
#         "faceId": "c5c24a82-6845-4031-9d5d-978df9175426",
#         "faceRectangle": {
#             "width": 78,
#             "height": 78,
#             "left": 394,
#             "top": 54
#         },
#         "faceLandmarks": {
#             "pupilLeft": {
#                 "x": 412.7,
#                 "y": 78.4
#             },
#             "pupilRight": {
#                 "x": 446.8,
#                 "y": 74.2
#             },
#             "noseTip": {
#                 "x": 437.7,
#                 "y": 92.4
#             },
#             "mouthLeft": {
#                 "x": 417.8,
#                 "y": 114.4
#             },
#             "mouthRight": {
#                 "x": 451.3,
#                 "y": 109.3
#             },
#             "eyebrowLeftOuter": {
#                 "x": 397.9,
#                 "y": 78.5
#             },
#             "eyebrowLeftInner": {
#                 "x": 425.4,
#                 "y": 70.5
#             },
#             "eyeLeftOuter": {
#                 "x": 406.7,
#                 "y": 80.6
#             },
#             "eyeLeftTop": {
#                 "x": 412.2,
#                 "y": 76.2
#             },
#             "eyeLeftBottom": {
#                 "x": 413.0,
#                 "y": 80.1
#             },
#             "eyeLeftInner": {
#                 "x": 418.9,
#                 "y": 78.0
#             },
#             "eyebrowRightInner": {
#                 "x": 4.8,
#                 "y": 69.7
#             },
#             "eyebrowRightOuter": {
#                 "x": 5.5,
#                 "y": 68.5
#             },
#             "eyeRightInner": {
#                 "x": 441.5,
#                 "y": 75.0
#             },
#             "eyeRightTop": {
#                 "x": 446.4,
#                 "y": 71.7
#             },
#             "eyeRightBottom": {
#                 "x": 447.0,
#                 "y": 75.3
#             },
#             "eyeRightOuter": {
#                 "x": 451.7,
#                 "y": 73.4
#             },
#             "noseRootLeft": {
#                 "x": 428.0,
#                 "y": 77.1
#             },
#             "noseRootRight": {
#                 "x": 435.8,
#                 "y": 75.6
#             },
#             "noseLeftAlarTop": {
#                 "x": 428.3,
#                 "y": 89.7
#             },
#             "noseRightAlarTop": {
#                 "x": 442.2,
#                 "y": 87.0
#             },
#             "noseLeftAlarOutTip": {
#                 "x": 424.3,
#                 "y": 96.4
#             },
#             "noseRightAlarOutTip": {
#                 "x": 446.6,
#                 "y": 92.5
#             },
#             "upperLipTop": {
#                 "x": 437.6,
#                 "y": 105.9
#             },
#             "upperLipBottom": {
#                 "x": 437.6,
#                 "y": 108.2
#             },
#             "underLipTop": {
#                 "x": 436.8,
#                 "y": 111.4
#             },
#             "underLipBottom": {
#                 "x": 437.3,
#                 "y": 114.5
#             }
#         },
#         "faceAttributes": {
#             "age": 71.0,
#             "gender": "male",
#             "smile": 0.88,
#             "facialHair": {
#                 "mustache": 0.8,
#                 "beard": 0.1,
#                 "sideburns": 0.02
#                 }
#             },
#             "glasses": "sunglasses",
#             "headPose": {
#                 "roll": 2.1,
#                 "yaw": 3,
#                 "pitch": 0
#             }
#         }
#     }
# ]
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def train_view(request):
    r = requests.get('http://172.25.0.5:5000/app/train')
    return Response({"status":r.text})

@api_view(['POST'])
def predict_view(request, text):
    r = requests.post(f'http://172.25.0.5:5000/app/predict/{text}')
    return Response(r.json())

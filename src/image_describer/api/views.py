from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import PredictionCreateSerializer


@api_view(["POST"])
def predict_image_title(request):
    serializer = PredictionCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        import ipdb

        ipdb.set_trace()
        # register task
        predicted_title = "OK"
        return Response({"title": predicted_title})

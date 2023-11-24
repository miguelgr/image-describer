from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from image_describer import tasks
from .serializers import PredictionCreateSerializer


@api_view(["POST"])
def predict_image_title(request):
    serializer = PredictionCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # Using .get() we wait for the worker result in a given TTL
        result = tasks.predict_image_title.delay(
            serializer.validated_data["image"]
        ).get()
        if result.ok:
            return Response({"title": "title"})
        return Response(status=400)

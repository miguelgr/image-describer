from rest_framework.response import Response
from rest_framework.decorators import api_view, throttle_classes

from .serializers import PredictionCreateSerializer


@api_view(["POST"])
def predict_image_title(request):
    # Get image from request
    serializer = PredictionCreateSerializer(**request.data)
    if serializer.is_valid(raise_exception=True):
        # register task
        pass

    return Response({"title": "Hello, world!"})

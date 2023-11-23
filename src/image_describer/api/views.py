from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from image_describer import tasks
from .serializers import PredictionCreateSerializer


@api_view(["POST"])
def predict_image_title(request):
    serializer = PredictionCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        result = tasks.predict_image_title.delay(image).get()
        import ipdb

        ipdb.set_trace()
        if result.ok:
            return Response({"title": result.value})
        return Response(status=400)

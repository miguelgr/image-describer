from django.urls import path

from .views import predict_image_title

app_name = "api"

urlpatterns = [path(r"predictions", predict_image_title)]

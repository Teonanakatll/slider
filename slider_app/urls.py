from django.urls import path

from slider_app.views import home, MessageView

urlpatterns = [
    path('', home, name='home'),
    path('message/', MessageView.as_view(), name='message'),
]
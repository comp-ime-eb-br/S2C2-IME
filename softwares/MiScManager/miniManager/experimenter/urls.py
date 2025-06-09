from django.urls import path, re_path
from .webSocketServer import WebSocketServer
from .views import RoundsView, RoundView, FinishRoundView, ExportRoundView, CompareRoundsView

urlpatterns = [
    path('rounds/<version_id>', RoundsView.as_view(), name='rounds'),
    path('round/<round_id>', RoundView.as_view(), name='round'),
    path('round/', RoundView.as_view(), name='round'),
    path('export-round/<round_id>', ExportRoundView.as_view()),
    path('compare-rounds/', CompareRoundsView.as_view()),
    path('finish-round', FinishRoundView.as_view()),
]

websocket_urlpatterns = [
    re_path(r'ws/round/(?P<round_id>\w+)/$', WebSocketServer.as_asgi()),
]
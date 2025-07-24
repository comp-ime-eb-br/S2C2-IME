from django.urls import path
from .views import HomeScenarioView, fetch_power_types, UploadScenarioView



urlpatterns = [
    path('index/', HomeScenarioView.homescenario, name='home_scenario'),
    path('upload_scenario/', UploadScenarioView.upload_scenario, name='home_scenario'),
    path('fetch_power_types/', fetch_power_types, name='fetch_power_types'),
#    path('page1/', TestPlanView.as_view(), name='test-plan'),
#    path('test-plans/', TestPlansView.as_view(), name='test-plans')
]
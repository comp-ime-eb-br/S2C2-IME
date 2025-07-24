from django.urls import path
from .views import VersionView, VersionsView, TestPlanView, TestPlansView, ExportVersionView, HomeView, AboutView, EditView, SupportView



urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('version/<test_plan_id>', VersionView.as_view(), name='version'),
    path('version/', VersionView.as_view(), name='version'),
    path('versions/<test_plan_id>', VersionsView.as_view(), name='versions'),
    path('export-version/<version_id>', ExportVersionView.as_view(), name='export-version'),
    path('test-plan/', TestPlanView.as_view(), name='test-plan'),
    path('test-plans/', TestPlansView.as_view(), name='test-plans'),
    path('about/', AboutView.about, name='about'),
    path('support/', SupportView.support, name='support'),
    path('versions/edit_version/<version_id>', EditView.edit_version, name='edit_version')
]
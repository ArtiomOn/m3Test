from django.conf.urls import url
from django.urls import include, path
from rest_framework_nested import routers

from apps.tasks.views import TaskViewSet, TaskFilterListView
from apps.tasks.views import CommentViewSet

tasks_router = routers.SimpleRouter()
tasks_router.register(r'tasks', TaskViewSet)

comments_router = routers.NestedSimpleRouter(tasks_router, r'tasks', lookup='task')
comments_router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('tasks/search/', TaskFilterListView.as_view()),
    url(r'', include(tasks_router.urls)),
    url(r'', include(comments_router.urls)),

]

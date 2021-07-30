from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')  # step 5, Using Router

urlpatterns = [
    # path("polls/", polls_list, name="polls_list"),  # step 1

    # path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),  # step 2

    # path("polls/", PollList.as_view(), name="polls_list"),  # step 3, Using generics
    # path("choices/", ChoiceList.as_view(), name="choice_list"),
    # path("vote/", CreateVote.as_view(), name="create_vote"),

    path("polls/<int:pk>/choices/", ChoiceList.as_view(),  # step 4, Changing the views
         name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/",
         CreateVote.as_view(), name="create_vote"),
]

urlpatterns += router.urls

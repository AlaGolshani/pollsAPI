from django.urls import path
from .views import polls_list, ChoiceList, CreateVote
from .views import PollList, PollDetail

urlpatterns = [
    # path("polls/", polls_list, name="polls_list"),  # step 1
    path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),  # step 2

    path("polls/", PollList.as_view(), name="polls_list"),  # step 3, Using generics
    path("choices/", ChoiceList.as_view(), name="choice_list"),
    path("vote/", CreateVote.as_view(), name="create_vote"),

]

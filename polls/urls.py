from django.urls import path
from .views import polls_list, polls_detail
from .views import PollList, PollDetail

urlpatterns = [
    # path("polls/", polls_list, name="polls_list"),  # step 1
    path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),  # step 2

    path("polls/", PollList.as_view(), name="polls_list"),  # step 3, Using generics

]

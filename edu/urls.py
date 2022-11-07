from django.urls import path
from django.views.generic import TemplateView

from edu.views.bartleby import BartlebyView
from edu.views.bot import BotCreateView, BotDeleteView, BotDetailView, BotListView, BotUpdateView
from edu.views.chegg import CheggView
from edu.views.plan import PlanCreateView, PlanDeleteView, PlanDetailView, PlanListView, PlanUpdateView
from edu.views.subscription import (SubscriptionCreateView, SubscriptionDeleteView, SubscriptionDetailView,
                                    SubscriptionListView, SubscriptionUpdateView)
from edu.views.assignment import (
                                AssignmentCreateView, AssignmentDeleteView, AssignmentDetailView, AssignmentListView, AssignmentUpdateView
                                )


urlpatterns = [
    path('chegg/', CheggView.as_view(), name='chegg_view'),
    path('bartleby/', BartlebyView.as_view(), name='bartleby_view'),
    path('bots/', BotListView.as_view(), name='bot_list_view'),
    path('bot/create/', BotCreateView.as_view(), name='bot_create_view'),
    path('bot/<int:pk>/', BotDetailView.as_view(), name='bot_detail_view'),
    path('bot/<int:pk>/update/', BotUpdateView.as_view(), name='bot_update_view'),
    path('bot/<int:pk>/delete/', BotDeleteView.as_view(), name='bot_delete_view'),
    path('plans/', PlanListView.as_view(), name='plan_list_view'),
    path('plan/create/', PlanCreateView.as_view(), name='plan_create_view'),
    path('plan/<int:pk>/', PlanDetailView.as_view(), name='plan_detail_view'),
    path('plan/<int:pk>/update/', PlanUpdateView.as_view(), name='plan_update_view'),
    path('plan/<int:pk>/delete/', PlanDeleteView.as_view(), name='plan_delete_view'),
    path('subscriptions/', SubscriptionListView.as_view(), name='subscription_list_view'),
    path('subscription/create/', SubscriptionCreateView.as_view(), name='subscription_create_view'),
    path('subscription/<int:pk>/', SubscriptionDetailView.as_view(), name='subscription_detail_view'),
    path('subscription/<int:pk>/update/', SubscriptionUpdateView.as_view(), name='subscription_update_view'),
    path('subscription/<int:pk>/delete/', SubscriptionDeleteView.as_view(), name='subscription_delete_view'),
    path('assignments/', AssignmentListView.as_view(), name='assignment_list_view'),
    path('assignment/create/', AssignmentCreateView.as_view(), name='assignment_create_view'),
    path('assignment/<int:pk>/', AssignmentDetailView.as_view(), name='assignment_detail_view'),
    path('assignment/<int:pk>/update/', AssignmentUpdateView.as_view(), name='assignment_update_view'),
    path('assignment/<int:pk>/delete/', AssignmentDeleteView.as_view(), name='assignment_delete_view'),

]

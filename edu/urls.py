from django.urls import path
from django.views.generic import TemplateView

from edu.views.bot import BotCreateView, BotDeleteView, BotDetailView, BotListView, BotUpdateView
from edu.views.chegg import CheggView
from edu.views.plan import PlanCreateView, PlanDeleteView, PlanDetailView, PlanListView, PlanUpdateView
from edu.views.subscription import (SubscriptionCreateView, SubscriptionDeleteView, SubscriptionDetailView,
                                    SubscriptionListView, SubscriptionUpdateView)

urlpatterns = [
    path('chegg/', CheggView.as_view(), name='chegg_view'),
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
]

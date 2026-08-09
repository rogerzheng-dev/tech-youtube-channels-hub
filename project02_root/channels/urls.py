from django.urls import path
from .views import (
    ChannelListView,
    ChannelDetailView,
    ChannelCreateView,
    ChannelUpdateView,
    ChannelDeleteView,
)

urlpatterns = [
    path('create/', ChannelCreateView.as_view(), name='channel_create'),
    path('<slug:slug>/edit/', ChannelUpdateView.as_view(), name='channel_update'),
    path('<slug:slug>/delete/', ChannelDeleteView.as_view(), name='channel_delete'),
    path('<slug:slug>/', ChannelDetailView.as_view(), name='channel_detail'),
    path('', ChannelListView.as_view(), name='channel_list'),
]
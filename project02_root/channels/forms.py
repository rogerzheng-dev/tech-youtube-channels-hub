from django import forms
from .models import Channel

class ChannelForm(forms.ModelForm):
    class Meta:
        model = Channel
        fields = ['name', 'slug', 'creator_name', 'category', 'description', 'subscribers', 'youtube_url', 'image']
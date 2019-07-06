from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'URL', 'youtube_id']
        labels = {'youtube_id':'YouTube ID', 'URL':'URL'}

class SearchForm(forms.Form):
    search_term = forms.CharField(max_length=255, label='Search for Videos')

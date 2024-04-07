from django import forms
from urlshortener.models import Shortener


class ShortenerForm(forms.ModelForm):
    long_url = forms.URLField(widget=forms.URLInput(
        attrs={"class": "url-input", "placeholder": "Your URL to shorten"}))

    class Meta:
        model = Shortener

        fields = ('long_url',)


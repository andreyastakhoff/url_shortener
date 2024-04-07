from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.views.generic.edit import CreateView

from urlshortener.models import Shortener
from urlshortener.forms import ShortenerForm

# Create your views here.

class ShortenerCreateView(CreateView):
    model = Shortener
    form_class = ShortenerForm

    def form_valid(self, form):
        shortener = form.save(commit=False)
        shortener.create_short_url()
        shortener.save()

        long_url = shortener.long_url
        new_url = self.request.build_absolute_uri('/') + shortener.short_url
        context = {
                "new_url": new_url,
                "long_url": long_url,
                "form": ShortenerForm(),
                }

        return render(self.request, 'urlshortener/shortener_form.html', context)


def redirect_url_view(request, shortened_part):
    try:
        shortener = Shortener.objects.get(short_url=shortened_part)
        shortener.times_followed += 1        
        shortener.save()
        
        return HttpResponseRedirect(shortener.long_url)
        
    except:
        raise Http404('Sorry this link is broken :(')

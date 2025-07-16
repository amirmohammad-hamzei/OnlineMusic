from channels.layers import get_channel_layer
from django.shortcuts import render
from django.views import View

from .api.stations import STATIONS, STREAMS


# Create your views here.

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'music/index.html')


class Player(View):
    def get(self, request):
        genre = request.GET.get('genre', 'phonk')
        stream_url = STREAMS.get(genre)
        if not stream_url:
            return render(request, 'music/player.html', {
                'error': 'Genre not found'
            })
        return render(request, 'music/player.html', {
            'genre': genre,
            'stream_url': stream_url
        })

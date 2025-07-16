from channels.layers import get_channel_layer
from rest_framework.views import APIView
from rest_framework.response import Response
import httpx

from .stations import STATIONS, STREAMS


class NowPlayingView(APIView):
    def get(self, request, *args, **kwargs):
        genre = request.query_params.get("genre", "phonk")
        api_url = STATIONS.get(genre)
        stream_url = STREAMS.get(genre)

        if not api_url:
            return Response({"error": "Genre not found"}, status=404)

        if not stream_url:
            return Response({"error": "Stream URL not found"}, status=404)

        try:
            response = httpx.get(api_url, timeout=5.0)
            response.raise_for_status()
            data = response.json()

            history = data["result"]["history"]
            current_song = history[0]

            return Response({"current": current_song, "stream_url": stream_url})
        except Exception as e:
            return Response({"error": str(e)}, status=500)

from django.views.generic import TemplateView

# Create your views here.
class FeedView(TemplateView):
    template_name = 'feed.html'

# Views:
# FeedView - Lista de posts
# PostView
# PostCreate
# PostUpdate - Tempo limite (10 min) - Marcação (edited) - Notificação para profiles que deram like
# PostDelete
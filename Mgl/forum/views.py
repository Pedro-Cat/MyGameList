from django.views.generic import TemplateView

# Create your views here.
class ForumView(TemplateView):
    template_name = 'forum.html'

# Views:
# ForumView
# PerguntaView
# PerguntaCreate
# PerguntaUpdate - Tempo limite (10 min) - Marcação (edited) - Bloco para updates pós tempo limite
# PerguntaDelete
# RespostaView
# RespostaCreate
# RespostaUpdate - Tempo limite (10 min) - Marcação (edited)
# RespostaDelete

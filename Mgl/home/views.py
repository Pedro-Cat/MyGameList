from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

# Views:
# HomeView - listas

# ListView - Alternar visibilidade entre lista maximizada e minimizada
# ListCreate
# ListUpdate 
# ListDelete

# JogoView - Alternar visibilidade entre jogo maximizado e minimizado, barra de pesquisa e profile
# JogoCreate
# JogoUpdate 
# JogoDelete

# BarraDePesquisaView
# BarraDePesquisaUpdate
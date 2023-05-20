from django.db import models

# Create your models here.
# Classes: 
# Pergunta {perfil, titulo, texto, arquivo, data-da-pergunta, upvote, downvote, tags} 
# Resposta {pergunta-relacionada, perfil, texto, arquivo, data-da-resposta, idPergunta, idResposta, upvote, downvote} -  Tentar juntar pergunta e resposta na mesma tabela. Caso contrário, criar métodos para diferenciar o id da pergunta e o id da resposta

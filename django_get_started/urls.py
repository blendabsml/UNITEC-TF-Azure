# -*- coding: utf-8 -*-

"""
Definition of urls for django_get_started.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm
from django.contrib import admin
from django.contrib.auth.views import login, logout
from app.views import *
from django.conf.urls.static import static
from django.conf import settings
from app.views import *

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="home"),
    url(r'^index/', index),
    url(r'^Contato/', Contato, name="Contato"),
    url(r'^curso/', curso),
    url(r'^entrar/', login,{"template_name":"login.html"}, name="login"),
    url(r'^sair/', logout, name="logout"),
    url(r'^ListaCursos/', ListaCurso),   
    url(r'^AreaAluno/', AreaAluno),      
    url(r'^Disciplinas/', Disciplinas),
    url(r'^noticia1/', noticia1),
    url(r'^noticia2/', noticia2),
    url(r'^Noticias/', Noticias),
    url(r'^SobreCurso/', SobreCurso),
    url(r'^restrito/$', restrito, name='restrito'),
    url(r'^restrito/(?P<sigla>[A-Z,a-z]+)/questao/(?P<questao_id>[0-9]*)', questao_form, name='questao_form'),
	url(r'^email/', email),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

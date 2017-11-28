# -*- coding: utf-8 -*-

"""
Definition of views.
"""

from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.template import RequestContext
from app.models import *
from datetime import datetime
from app.models import *
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage
from app.forms import *

def index(request):
    return render(request, "index.html")

#Função de formulário contato, caso válido enviará um email para o retorno do campo "Email"
def Contato(request):
    #importando formulário "ContatoForm"
    form = ContatoForm
    #checagem de validação do formulário
    if request.method == 'POST':
        form = form(data=request.POST)
        #Se é válido, receber os campos e adicioná-los em variáveis
        if form.is_valid():
            Nome_Completo = request.POST.get(
                'Nome_Completo'
            , '')
            Telefone = request.POST.get(
                'Telefone'
            , '')
            Email = request.POST.get(
                'Email'
            , '')
            #Construção do corpo de email e envio do mesmo, e retornando a página de Contato após a operação
            Assunto_Contato = request.POST.get('Assunto_Contato', '')
            Mensagem = request.POST.get('Mensagem', '')
            Mensagem_corpo = "Nome: " + Nome_Completo + " \n" + "Telefone: " + Telefone  + " \n" + "Assunto do Contato: " + Assunto_Contato + " \n" + " \n" + Mensagem 
            subject = 'Formulario de Contato'
            from_email = settings.EMAIL_HOST_USER
            to_list = [Email]
            send_mail(subject, Mensagem_corpo, from_email, to_list, fail_silently=True)
    return render(request, 'Contato.html', {
    'form': form,
    })

#Curso, Validando formulário e retornando a renderização da página
def curso(request):
    if request.POST:    
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = CursoForm()

    contexto = {
        "form": form
    }
    return render(request, "curso.html", contexto)

#retornando a renderização da página
def ListaCurso(request):
    return render(request, "ListaCursos.html")

def AreaAluno(request):
    form = EmailForm
    if request.method == 'POST':
        form = form(data=request.POST)
        if form.is_valid():
            nome = request.POST.get(
                'nome'
            , '')
            email = request.POST.get(
                'email'
            , '')
            mensagem = request.POST.get('mensagem', '')
            subject = 'Faculdade Unitec'
            from_email = settings.EMAIL_HOST_USER
            to_list = [email]
            send_mail(subject, mensagem,from_email, to_list, fail_silently=True)
    return render(request, 'AreaAluno.html', {
    'form': form,
    })

#Função de Upload de imagem

    # if request.method == 'POST' and request.FILES['myfile']:
        # myfile = request.FILES['myfile']
        # fs = FileSystemStorage()
        # filename = fs.save(myfile.name, myfile)
        # uploaded_file_url = fs.url(filename)
        # return render(request, 'AreaAluno.html', {
            # 'uploaded_file_url': uploaded_file_url
        # })
    # return render(request, "AreaAluno.html")

#retornando a renderização da página
def Disciplinas(request):
    return render(request, "Disciplinas.html")

#retornando a renderização da página
def noticia1(request):
    return render(request, "noticia1.html")

#retornando a renderização da página
def noticia2(request):
    return render(request, "noticia2.html")

#retornando a renderização da página
def Noticias(request):
    return render(request, "Noticias.html")

#retornando a renderização da página
def SobreCurso(request):
    return render(request, "SobreCurso.html")

#Teste de upload de imagem
def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'simple_upload.html')

def restrito(request):
#    cursos = Curso.objects.all()
#    for curso in cursos:
#        curso.questoes = Questao.objects.filter(curso=curso)

#    contexto = {
#        "cursos":cursos
#    }
    return render(request, "restrito.html")

def questao_form(request, sigla, questao_id=None):
    curso = Curso.objects.get(sigla=sigla)
    if questao_id:
            questao = Questao.objects.get(id=questao_id)
    else:
        questao = Questao(curso=curso)

    if request.POST:
        form = QuestaoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/restrito')
    else:

        form = QuestaoForm(instance=questao)

    contexto = {
        "form": form,
        "curso": curso
    }
    return render(request, "questao_form.html", contexto)

def email(request):
    form = EmailForm
    if request.method == 'POST':
        form = form(data=request.POST)

        if form.is_valid():
            nome = request.POST.get(
                'nome'
            , '')
            email = request.POST.get(
                'email'
            , '')
            mensagem = request.POST.get('mensagem', '')
            subject = 'Faculdade Unitec'
            from_email = settings.EMAIL_HOST_USER
            to_list = [email]
            send_mail(subject, mensagem,from_email, to_list, fail_silently=True)
    return render(request, 'email.html', {
    'form': form,
    })

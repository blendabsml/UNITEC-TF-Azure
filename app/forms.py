# -*- coding: utf-8 -*-

"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from app.models import Document, Questao, Curso, Aluno

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

    
#Formulário de Curso, Considerando todos os campos
class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = "__all__"

#Formulário de Contato, usado para envio
class ContatoForm(forms.Form):
    Nome_Completo = forms.CharField(required=True)
    Telefone = forms.IntegerField(required=True)
    Email = forms.EmailField(required=True)
    Assunto_Contato = forms.CharField(required=True)
    Mensagem = forms.CharField(required=True, widget=forms.Textarea)

#Formulário de Email, usado para envio
class EmailForm(forms.Form):
    nome = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    mensagem = forms.CharField(required=True, widget=forms.Textarea)

#Formulário de Documento, Considerando todos os campos
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )

#Formulário de Questãp, usando um modelo de "Questão", criado em models.py, excluindo "curso" dos campos
class QuestaoForm(forms.ModelForm):
      class Meta:
        model = Questao
        exclude = ["curso"]

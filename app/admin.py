# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app.models import *
from django import forms

#Essas funções serão apresentadas no menu ADMIN do site

#Função Novo Aluno, com quais campos serão requisitados
# class NovoAlunoForm(forms.ModelForm):
#     class Meta:	
#         model = Aluno    
#         fields = ('ra', 'nome','curso')

#     #Ao finalizar, já vem com uma senha pré-definida
#     def save(self, commit=True):
#         user = super(NovoAlunoForm, self).save(commit=False)
#         user.set_password('123@mudar')
#         user.perfil = 'A'        
#         if commit:           
#             user.save()        
#         return user

#Função AlteraAluno, podendo alterar apenas Nome, e Curso
# class AlterarAlunoForm(forms.ModelForm):
#      class Meta:
#         model = Aluno         
#         fields = ('nome', 'curso')

#Função principal de criação de aluno, e a forma que será visualizado
#class AlunoAdmin(UserAdmin):
#     form = AlterarAlunoForm    
#     add_form = NovoAlunoForm
#     list_display = ('ra', 'nome', 'email', 'curso')
#     list_filter = ('perfil',)
#     fieldsets = ( (None, {'fields': ('ra', 'nome', 'email', 'curso')}),)
#     add_fieldsets = ((None, { 'fields': ('ra', 'nome', 'email', 'curso')} ),)
#     search_fields = ('ra',)
#     ordering = ('ra',)
#     filter_horizontal = ()

#Função Curso, e quais campos serão apresentados
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome','tipo', 'carga_horaria')
    list_filter = ('tipo',)

#Função Disciplina, e quais campos serão apresentados, ou usados na busca
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'carga_horaria', 'teoria')
    list_display = ('nome',)
    search_fields = ('nome',)

#Função Professor, e quais campos serão apresentados após criação
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ra', 'email',)

#Função Turma, e quais campos serão apresentados após criação
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('professor', 'turma_sigla', 'turno',)

#Função Disciplina Ofertada, que usa o cadastro de Disciplina
class DisciplinaOfertadaAdmin(admin.ModelAdmin):
    list_display = ('disciplina', 'ano', 'semestre',)

#Função Grade Curricular, e quais campos serão apresentados após criação 
class GradeCurricularAdmin(admin.ModelAdmin):
    list_display = ('curso', 'ano', 'semestre',)

#Função Período, que usa Grade Curricular 
class PeriodoAdmin(admin.ModelAdmin):
    list_display = ('gradeCurricular', 'numero',)

#Função que apenas registra o campo de Arquivo
class ArquivosFotoAdmin(admin.ModelAdmin):
    list_display = ('arquivo',)

#Função Candidato, e quais campos serão apresentados após criação
class CandidatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'confirmado',)

#Função Questão, e quais campos serão apresentados após criação, depende de Arquivo Questão
class QuestaoAdmin(admin.ModelAdmin):
    list_display = ('turma', 'id', 'descricao')

#Função Arquivos Questão, que apenas registra o campo de Arquivos
class ArquivosQuestaoAdmin(admin.ModelAdmin):
    list_display = ('questao', 'id')

#Função Arquivos Resposta, e quais campos serão apresentados após criação
class RespostaAdmin(admin.ModelAdmin):
    list_display = ('questao', 'descricao')

#Função Arquivo Resposta
class ArquivosRespostaAdmin(admin.ModelAdmin):
    list_display = ('resposta', 'id')

#Relacionamentos entre funções e modelos criados no arquivo models.py
#admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Turma, TurmaAdmin)
admin.site.register(DisciplinaOfertada, DisciplinaOfertadaAdmin)
admin.site.register(GradeCurricular, GradeCurricularAdmin)
admin.site.register(Periodo, PeriodoAdmin)
admin.site.register(ArquivosFoto, ArquivosFotoAdmin)
admin.site.register(Candidato, CandidatoAdmin)
admin.site.register(Questao, QuestaoAdmin)
admin.site.register(ArquivosQuestao, ArquivosQuestaoAdmin)
admin.site.register(Resposta, RespostaAdmin)
admin.site.register(ArquivosResposta, ArquivosRespostaAdmin)

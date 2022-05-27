from django import forms
from django.core.mail.message import EmailMessage
from .models import *
from django.forms import ModelForm

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail',max_length=100)
    assunto = forms.CharField(label='Assunto',max_length=100)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome:{nome}\nE-mail:{email}\nAssunto:{assunto}\nMensagem:{mensagem}'

        mail = EmailMessage(
            subject=assunto,
            body=conteudo,
            from_email='contato@seudomino.com',
            to=['danielferrangel.98@gmail.com'],
            headers={'Reply-to': email}
        )
        mail.send()

class RegistroForm(ModelForm):

    class Meta:
        model = Morador
        fields = ('nome', 'idade', 'endereco','sexo')

"""class OrigemForm(ModelForm):
    class Meta:
        model = Origem
        fields = ('id','naturalidade', 'descricao', 'tempRua', 'porque')

class ResidenciaForm(ModelForm):
    class Meta:
        model = Residencia
        fields = ('id','residen', 'local')

class IdentificacaoForm(ModelForm):
    class Meta:
        model = Identificacao
        fields = ('id','documento', 'documentos')

class FamiliaresForm(ModelForm):
    class Meta:
        model = Familiares
        fields = ('id','familia', 'onde', 'composta', 'outros')

class SaudeForm(ModelForm):
    class Meta:
        model = Saude
        fields = ('id','vacinado', 'vacinas', 'dose','outros', 'dependente', 'drogas', 'outra', 'tratamento', 'ondeTrata', 'doenca', 'qual', 'tratamentoDoenca', 'onde')

class ReligiaoForm(ModelForm):
    class Meta:
        model = Religiao
        fields = ('id','crenca', 'religiosidade')

class ProfissionalForm(ModelForm):
    class Meta:
        model = Profissional
        fields = ('id','profissao', 'qual', 'trabalha','emque', 'trabalhou', 'doque', 'aprender')

class EscolaridadeForm(ModelForm):
    class Meta:
        model = Escolaridade
        fields = ('id','alfabetisado', 'grau', 'profissionalizante')"""

class FichaForm(ModelForm):
    class Meta:
        model = FichaRegistros
        fields = '__all__'


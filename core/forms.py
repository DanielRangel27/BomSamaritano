from django import forms
from django.core.mail.message import EmailMessage
from .models import Morador,Familia
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
        fields = ('nome', 'idade', 'endereco')
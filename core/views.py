from django.shortcuts import render,redirect
from django.views.generic import FormView, TemplateView
from .models import Morador, Familia
from .forms import ContatoForm, RegistroForm
from django.contrib import messages
from django.urls import reverse_lazy

class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso!')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar e-mail')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)

class RegistroView(FormView):
    template_name = 'registro.html'
    form_class = RegistroForm
    success_url = reverse_lazy('registro')

    def Registrar(request):
        if request.method == 'POST':
            form = RegistroForm(request.POST)

            if form.is_valid():
                form.save()
        return render(request, 'registro.html', {'form': form})
from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic.edit import FormView, CreateView
from .forms import *
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from .models import *

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

def Formulario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registro')
        else:
            return redirect('form1')
    else:
        form = RegistroForm()
        return render(request, 'form1.html',
                      {'form': form})
def Registrar(request):
    if request.method == 'POST':
        form_ficha = FichaForm(request.POST)
        naturalidade = request.POST.get('naturalidade')
        descricao = request.POST.get('descricao')
        tempRua = request.POST.get('tempRua')
        porque = request.POST.get('porque')
        residen = request.POST.get('residen')
        local = request.POST.get('local')
        documento = request.POST.get('documento') == 'on'
        documentos = request.POST.get('documentos')
        familia = request.POST.get('familia') == 'on'
        ondeFami = request.POST.get('ondeFami')
        composta = request.POST.get('composta')
        outrosFami = request.POST.get('outrosFami')
        vacinado = request.POST.get('vacinado') == 'on'
        vacinas = request.POST.get('vacinas')
        dose = request.POST.get('dose')
        outrosVacina = request.POST.get('outrosVacina')
        dependente = request.POST.get('dependente') == 'on'
        drogas = request.POST.get('drogas')
        outraDroga = request.POST.get('outraDroga')
        tratamento = request.POST.get('tratamento') == 'on'
        ondeTrata = request.POST.get('ondeTrata')
        doenca = request.POST.get('doenca') == 'on'
        qualDoenca = request.POST.get('qualDoenca')
        tratamentoDoenca = request.POST.get('tratamentoDoenca') == 'on'
        ondeTratamento = request.POST.get('ondeTratamento')
        crenca = request.POST.get('crenca') == 'on'
        religiosidade = request.POST.get('religiosidade')
        profissao = request.POST.get('profissao') == 'on'
        qualProfi = request.POST.get('qualProfi')
        trabalha = request.POST.get('trabalha') == 'on'
        emque = request.POST.get('emque')
        trabalhou = request.POST.get('trabalhou') == 'on'
        doque = request.POST.get('doque')
        aprender = request.POST.get('aprender')
        alfabetisado = request.POST.get('alfabetisado') == 'on'
        grau = request.POST.get('grau')
        profissionalizante = request.POST.get('profissionalizante')
        morador_id = request.POST.get("id")
        morador = Morador.objects.get(id=morador_id)

        FichaRegistros.objects.create(
            naturalidade = naturalidade,
            descricao =descricao,
            tempRua = tempRua,
            porque = porque,
            residen = residen,
            local =local,
            documento = documento,
            documentos =documentos,
            familia =familia,
            ondeFami =ondeFami,
            composta =composta,
            outrosFami =outrosFami,
            vacinado =vacinado,
            vacinas =vacinas,
            dose =dose,
            outrosVacina =outrosVacina,
            dependente =dependente,
            drogas =drogas,
            outraDroga =outraDroga,
            tratamento =tratamento,
            ondeTrata =ondeTrata,
            doenca =doenca,
            qualDoenca =qualDoenca,
            tratamentoDoenca =tratamentoDoenca,
            ondeTratamento =ondeTratamento,
            crenca =crenca,
            religiosidade =religiosidade,
            profissao =profissao,
            qualProfi =qualProfi,
            trabalha =trabalha,
            emque =emque,
            trabalhou =trabalhou,
            doque =doque,
            aprender =aprender,
            alfabetisado =alfabetisado,
            grau =grau,
            profissionalizante =profissionalizante,

            id=morador
        )


        if form_ficha.is_valid():
            form_ficha.save()

        return redirect('form1')

    else:
        form_ficha = FichaForm()
        messages.error(request, 'Deu ruim')
        return render(request, 'registro.html',
                      {'morador': Morador.objects.all(),'form_ficha': form_ficha})


def telabusca(request):

    return render(request, 'busca.html', {'morador': Morador.objects.all()})
    if request.method == 'POST':

        id = request.POST.get('id', '')
        print(id)
        busca = Morador.objects.get(id=id)

        return render(request, 'informacoes.html', {'busca':busca})
def telabusca2(request):
    id = request.POST.get('id','')
    busca2 = FichaRegistros.objects.get(id=id)

    return render(request,'busca.html',{'busca2':busca2})

def telabuscaView(request, id):
    busca = get_object_or_404(Morador, pk=id)
    busca2 = get_object_or_404(FichaRegistros, pk=id)
    return render(request,'informacoes.html', {'busca': busca, 'busca2': busca2})
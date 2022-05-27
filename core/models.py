from pyexpat import model
from django.db import models





class Base(models.Model):
    criados = models.DateField("Criação", auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Morador(Base):
    id = models.AutoField('ID', primary_key=True)
    nome = models.CharField('Nome', max_length=100)
    idade = models.IntegerField('Idade', )
    endereco = models.CharField('Endereço', max_length=200)
    data = models.DateField('Data de Criação', auto_now_add=True)
    SEXO_CHOICES = (
        ('H', 'Homem'),
        ('M', 'Mulher'),
    )
    sexo = models.CharField(max_length=10, choices=SEXO_CHOICES)
    

    class Meta:
        verbose_name = 'Morador'
        verbose_name_plural = 'Moradores'

    def __str__(self):
        return self.nome

"""class Origem(Base):
    id = models.ForeignKey('Moradores', verbose_name='Morador', on_delete=models.CASCADE, primary_key=True)
    naturalidade = models.CharField('Naturalidade', max_length=200)
    descricao = models.CharField('Se não for de campos.../Quando veio??/Por que?', max_length= 500)
    tempRua = models.IntegerField('Tempo de Rua',)
    porque = models.CharField('O Por quê de esta na rua', max_length = 400)
    
    class Meta:
        verbose_name = 'Origem'
        verbose_name_plural = 'Origens'

    def __str__(self):
        return str(self.id)

class Residencia(Base):
    id = models.ForeignKey('Moradores', verbose_name='Morador', on_delete=models.CASCADE, primary_key=True)
    CASA_CHOICES = (
        ('C', 'Casa'),
        ('R', 'Rua'),
    )
    residen = models.CharField(max_length=10, choices=CASA_CHOICES)
    local = models.CharField('Local onde dorme',max_length=200)

    
    class Meta:
        verbose_name = 'Residencia'
        verbose_name_plural = 'Residensias'

    def __str__(self):
        return str(self.id)

class Identificacao(Base):
    id = models.ForeignKey('Moradores', verbose_name='Morador', on_delete=models.CASCADE, primary_key=True)
    documento = models.BooleanField('Possui documento?', default = False)
    IDENTIFICACAO_CHOICES2 = (
        ('CTPS', 'CTPS'),
        ('IDENTIDADE', 'IDENTIDADE'),
        ('TITULO', 'TITULO ELEITOR'),
        ('CPF', 'CPF'),
        ('HABILITACAO', 'HABILITAÇÃO'),
        ('RESERVISTA', 'CERTIFICADO DE RESERVISTA'),
    )
    documentos = models.CharField(max_length=50, choices=IDENTIFICACAO_CHOICES2,default='CPF')
    

    
    class Meta:
        verbose_name = 'Indentificação'
        verbose_name_plural = 'Identificações'

    def __str__(self):
        return str(self.id)

class Familiares(Base):
    id = models.ForeignKey('Moradores', verbose_name='Morador', on_delete=models.CASCADE, primary_key=True)
    familia = models.BooleanField('Possui família?', default = False)
    onde = models.CharField('Onde mora?', max_length=200)
    FAMILIA_CHOICES = (
        ('Pais', 'Pais'),
        ('Irmãos', 'Irmãos'),
        ('Cônjuge', 'Cônjuge'),
        ('Filhos', 'Filhos'),
        ('Outros', 'Outros'),
    )
    composta = models.CharField(max_length=20, choices=FAMILIA_CHOICES)
    outros = models.CharField('outros', max_length=100)
    
    class Meta:
        verbose_name = 'Família'
        verbose_name_plural = 'Familiares'

    def __str__(self):
        return str(self.id)

class Saude(Base):
    id = models.ForeignKey('Moradores', verbose_name='Morador', on_delete=models.CASCADE, primary_key=True)
    vacinado = models.BooleanField('Vacinado?', default = False)
    VACINA_CHOICES2 = (
        ('COVID', 'COVID'),
        ('INFLUENZA', 'INFLUENZA'),
        ('Outras', 'Outras'),
    )
    vacinas = models.CharField(max_length=20, choices=VACINA_CHOICES2)
    DOSE_CHOICES = (
        ('1ºD', '1dose'),
        ('2ºD', '2dose'),
        ('3ºD', '3dose'),
    )
    dose = models.CharField(max_length=10, choices=DOSE_CHOICES)
    outros = models.CharField('Outras', max_length=100)
    dependente = models.BooleanField('Depentente químico?', default=False)
    CATEGORY_CHOICES3 = (
        ('Álcool', 'Álcool'),
        ('Cocaína', 'Cocaína'),
        ('Crack', 'Crack'),
        ('Maconha', 'Maconha'),
    )
    drogas = models.CharField(max_length=10, choices=CATEGORY_CHOICES3,default='Álcool')
    outra = models.CharField('Outra',max_length=100)
    tratamento = models.BooleanField('Fez ou faz tratemento?', default=False)
    ondeTrata = models.CharField('Onde?', max_length=200)
    doenca = models.BooleanField('Tem enfermidade ou doença crônica?', default=False)
    qual = models.CharField('Qual?', max_length=200)
    tratamentoDoenca = models.BooleanField('Faz ou Fez tratamento?', default=False)
    onde = models.CharField('Onde?', max_length=100)

    
    class Meta:
        verbose_name = 'Saúde'
        verbose_name_plural = 'Saúdes'

    def __str__(self):
        return str(self.id)

class Religiao(Base):
    id = models.ForeignKey('Moradores', verbose_name='Morador', on_delete=models.CASCADE, primary_key=True)
    crenca = models.BooleanField('Possui alguma crença?', default = False)
    RELIGIAO_CHOICES2 = (
        ('Católica', 'Católica'),
        ('Evangélica', 'Evangélica'),
        ('Espirita', 'Espirita'),
        ('Umbanda', 'Umbanda'),
        ('Nenhuma', 'Nemnhuma'),
    )
    religiosidade = models.CharField(max_length=20, choices=RELIGIAO_CHOICES2)
    
    class Meta:
        verbose_name = 'Religião'
        verbose_name_plural = 'Religiões'

    def __str__(self):
        return str(self.id)

class Profissional(Base):
    id = models.ForeignKey('Moradores', verbose_name='Morador', on_delete=models.CASCADE, primary_key=True)
    profissao = models.BooleanField('Possui alguma Profissão?', default = False)
    qual = models.CharField('Qual?', max_length=100)
    trabalha = models.BooleanField('Trabalha atualmente?', default = False)
    emque = models.CharField('Em que?', max_length=200)
    trabalhou = models.BooleanField('Já trabalhou?', default = False)
    doque = models.CharField('Trabalhou em que?', max_length=200)
    aprender = models.CharField('O que gostaria de aprender?', max_length=100)
    
    class Meta:
        verbose_name = 'Profissional'
        verbose_name_plural = 'Profissionais'

    def __str__(self):
        return str(self.id)

class Escolaridade(Base):
    id = models.ForeignKey('Moradores', verbose_name='Morador', on_delete=models.CASCADE, primary_key=True)
    alfabetisado = models.BooleanField('Alfabetizado?', default = False)
    GRAU_CHOICES2 = (
        ('Fundaemental,Incompleto', 'Fun/Inc'),
        ('Fundamental,Completo', 'Fun/Com'),
        ('Médio,Incompleto', 'Médio/Inc'),
        ('Médio,Completo', 'Médio/Com'),
        ('Profissionalizante', 'Profissionalizante'),
    )
    grau = models.CharField(max_length=30, choices=GRAU_CHOICES2)
    profissionalizante = models.CharField('Qual Curso Profissionalizante?', max_length=100)

    
    class Meta:
        verbose_name = 'Escolaridade'
        verbose_name_plural = 'Escolaridades'

    def __str__(self):
        return str(self.id)"""
class FichaRegistros(Base):
    id = models.OneToOneField('Morador', verbose_name='Morador', on_delete=models.CASCADE, primary_key=True)
    naturalidade = models.CharField('Naturalidade', max_length=200)
    descricao = models.CharField('Se não for de campos.../Quando veio??/Por que?', max_length=500)
    tempRua = models.IntegerField('Tempo de Rua', )
    porque = models.CharField('O Por quê de esta na rua', max_length=400)
    CASA_CHOICES = (
        ('C', 'Casa'),
        ('R', 'Rua'),
    )
    residen = models.CharField(max_length=10, choices=CASA_CHOICES)
    local = models.CharField('Local onde dorme', max_length=200)
    documento = models.BooleanField('Possui documento?', default=False)
    IDENTIFICACAO_CHOICES2 = (
        ('CTPS', 'CTPS'),
        ('IDENTIDADE', 'IDENTIDADE'),
        ('TITULO', 'TITULO ELEITOR'),
        ('CPF', 'CPF'),
        ('HABILITACAO', 'HABILITAÇÃO'),
        ('RESERVISTA', 'CERTIFICADO DE RESERVISTA'),
    )
    documentos = models.CharField(max_length=50, choices=IDENTIFICACAO_CHOICES2, default='CPF')
    familia = models.BooleanField('Possui família?', default=False)
    ondeFami = models.CharField('Onde mora?', max_length=200)
    FAMILIA_CHOICES = (
        ('Pais', 'Pais'),
        ('Irmãos', 'Irmãos'),
        ('Cônjuge', 'Cônjuge'),
        ('Filhos', 'Filhos'),
        ('Outros', 'Outros'),
    )
    composta = models.CharField(max_length=20, choices=FAMILIA_CHOICES)
    outrosFami = models.CharField('outros', max_length=100)
    vacinado = models.BooleanField('Vacinado?', default=False)
    VACINA_CHOICES2 = (
        ('COVID', 'COVID'),
        ('INFLUENZA', 'INFLUENZA'),
        ('Outras', 'Outras'),
    )
    vacinas = models.CharField(max_length=20, choices=VACINA_CHOICES2)
    DOSE_CHOICES = (
        ('1ºD', '1dose'),
        ('2ºD', '2dose'),
        ('3ºD', '3dose'),
    )
    dose = models.CharField(max_length=10, choices=DOSE_CHOICES)
    outrosVacina = models.CharField('Outras', max_length=100)
    dependente = models.BooleanField('Depentente químico?', default=False)
    CATEGORY_CHOICES3 = (
        ('Álcool', 'Álcool'),
        ('Cocaína', 'Cocaína'),
        ('Crack', 'Crack'),
        ('Maconha', 'Maconha'),
    )
    drogas = models.CharField(max_length=10, choices=CATEGORY_CHOICES3, default='Álcool')
    outraDroga = models.CharField('Outra', max_length=100)
    tratamento = models.BooleanField('Fez ou faz tratemento?', default=False)
    ondeTrata = models.CharField('Onde?', max_length=200)
    doenca = models.BooleanField('Tem enfermidade ou doença crônica?', default=False)
    qualDoenca = models.CharField('Qual?', max_length=200)
    tratamentoDoenca = models.BooleanField('Faz ou Fez tratamento?', default=False)
    ondeTratamento = models.CharField('Onde?', max_length=100)
    crenca = models.BooleanField('Possui alguma crença?', default=False)
    RELIGIAO_CHOICES2 = (
        ('Católica', 'Católica'),
        ('Evangélica', 'Evangélica'),
        ('Espirita', 'Espirita'),
        ('Umbanda', 'Umbanda'),
        ('Nenhuma', 'Nenhuma'),
    )
    religiosidade = models.CharField(max_length=20, choices=RELIGIAO_CHOICES2)
    profissao = models.BooleanField('Possui alguma Profissão?', default=False)
    qualProfi = models.CharField('Qual?', max_length=100)
    trabalha = models.BooleanField('Trabalha atualmente?', default=False)
    emque = models.CharField('Em que?', max_length=200)
    trabalhou = models.BooleanField('Já trabalhou?', default=False)
    doque = models.CharField('Trabalhou em que?', max_length=200)
    aprender = models.CharField('O que gostaria de aprender?', max_length=100)
    alfabetisado = models.BooleanField('Alfabetizado?', default=False)
    GRAU_CHOICES2 = (
        ('Fundaemental,Incompleto', 'Fun/Inc'),
        ('Fundamental,Completo', 'Fun/Com'),
        ('Médio,Incompleto', 'Médio/Inc'),
        ('Médio,Completo', 'Médio/Com'),
        ('Profissionalizante', 'Profissionalizante'),
    )
    grau = models.CharField(max_length=30, choices=GRAU_CHOICES2)
    profissionalizante = models.CharField('Qual Curso Profissionalizante?', max_length=100)

    class Meta:
        verbose_name = 'FichaRegistro'
        verbose_name_plural = 'FichasRegistro'

    def __str__(self):
        return str(self.id)
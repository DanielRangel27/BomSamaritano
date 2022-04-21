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

    class Meta:
        verbose_name = 'Morador'
        verbose_name_plural = 'Moradores'

    def __str__(self):
        return self.nome


class Familia(Base):
    id = models.OneToOneField('core.Morador', verbose_name='Morador', on_delete=models.CASCADE, primary_key=True)

    familia = models.TextField('Dependentes', max_length=200)
    tempo = models.DateField('Tempo de Rua', auto_now=False, auto_now_add=False)
    usuario = models.BooleanField('Usuario Quimico', default=False)

    class Meta:
        verbose_name = 'Família'
        verbose_name_plural = 'Famílias'

    def __str__(self):
        return str(self.id)

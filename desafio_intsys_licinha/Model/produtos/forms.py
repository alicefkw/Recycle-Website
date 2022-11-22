from django.forms import ModelForm, DateInput 
from .models import Produtos

class DateInput(DateInput):
    input_type = 'date'

class FormProdutos(ModelForm):
    class Meta:
        model = Produtos
        fields = ['nome', 'quantidade', 'cidade', 'rua', 'agendamento']
        widgets = {
            'agendamento': DateInput(),
        }

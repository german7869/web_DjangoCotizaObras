from django import forms
from .models import Cotizacion
from django.forms.widgets import NumberInput
from django.forms import ModelForm

class Cotizacion_forms(forms.ModelForm):
      
      fecha_emision = forms.DateField(
        required=False,
        label="Fecha de emision" 
        )
      id_cliente = forms.CharField(
        required=True,
        label="cliente" 
        


        
        )
     

      class Meta:
        model = Cotizacion
        fields = ['fecha_emision','numero','id_cliente','total']
        
      def __init__(self, *args, **kwargs):

        super(Cotizacion_forms,self).__init__(*args, **kwargs)
        self.fields['fecha_emision'].widget.attrs['placeholder'] = 'dd/mm/yyyt'
        self.fields['id_cliente'].widget.attrs['placeholder'] = 'busque Nombre cliente'
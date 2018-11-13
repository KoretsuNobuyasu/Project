from django import forms
from .models import Expeditionreport



class ExpeditionreportCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
        self.fields['file'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Expeditionreport
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'file': forms.FileInput(attrs={
                'class': "form-control",
            }),
        }

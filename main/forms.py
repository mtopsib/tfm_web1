from .models import GrpStatDown, TechType, WorkArea, TechRole, Vinechikle, StateDown, DownTimeJornal, UpTimeJornal
from django.forms import ModelForm, TextInput, Textarea, ChoiceField

'''
class TaskForm(ModelForm):
    class Meta:
        pass
        
        model = Task
        fields = ['title', 'task']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            'task': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            })
        }
'''

'''
class InDataForm(ModelForm):
    class Meta:
        pass
        
        model = downtimejornal1

        fields = ['techtype', 'region', 'garnum', 'downdatetime']
        widgets = {
            'garnum': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            })

        }
'''






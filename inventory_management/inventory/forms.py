from django import forms
from .models import ExardProduct #, AssemblyProduct


# class AddProductForm(forms.ModelForm): 
#     class Meta:
#         model = ExardProduct
#         fields = ('alpha_number', 'quantity')


from django import forms
from .models import ExardProduct

class AddExhardForm(forms.ModelForm):
    alpha_number = forms.CharField(max_length=100, label="Alpha Number")    
    quantity = forms.IntegerField(min_value=1, label="Quantity to Add")

    class Meta:
        model = ExardProduct
        fields = ['alpha_number', 'quantity']


# class AddAssemblyForm(forms.ModelForm):
#     alpha_number = forms.ModelChoiceField(max_length=100, label="Alpha Number")
#     bap_number = forms.CharField(max_length=100, label="BAP Number")
#     quantity = forms.IntegerField(min_value=1, label="Quantity to Add")

#     class Meta:
#         model = AssemblyProduct
#         fields = ['alpha_number', 'bap_number', 'quantity']


# from django import forms
# from .models import ExardProduct

# class AddExhardForm(forms.ModelForm):
#     class Meta:  
#         model = ExardProduct
#         fields = ['alpha_number', 'quantity']
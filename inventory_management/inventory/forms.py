from django import forms
from .models import ExardProduct


class AddProductForm(forms.ModelForm): 
    class Meta:
        model = ExardProduct
        fields = ('alpha_number', 'quantity')




from .models import ExardProduct


class AddExhardForm(forms.Form):
    alpha_number = forms.ModelChoiceField(queryset=ExardProduct.objects.all(), label="Alpha Number")
    quantity = forms.IntegerField(min_value=1, label="Quantity to Add")



# from django import forms
# from .models import ExardProduct

# class AddExhardForm(forms.ModelForm):
#     class Meta:
#         model = ExardProduct
#         fields = ['alpha_number', 'quantity']
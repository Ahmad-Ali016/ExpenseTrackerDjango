from django.forms import ModelForm
from core.models import Expense
from django import forms

class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ["name","amount", "category", "tags"]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter amount'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
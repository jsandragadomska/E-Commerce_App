from django import forms

class ProductForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField()
    amount = forms.IntegerField()
from django import forms

from .models import Product, Category

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title', 'content', 'price', 'amount', 'category'
        ]

        widgets = {
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
        }
    
    def clean_title(self):
        data = self.cleaned_data.get('title')
        if len(data) < 6:
            raise forms.ValidationError("This is not long enaugh")
        return data
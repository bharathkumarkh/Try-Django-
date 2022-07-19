from django import forms
from .models import Recipe, RecipeIngredient, RecipeIngredientImage

class RecipeIngredientImageForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredientImage
        fields = ['image']
        labels={
            "image":"Extract Via Image Upload"
        }

class RecipeForm(forms.ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required-field'
    # name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control","placeholder":"Recipe/Dish Name"})) #Input Field
    # description = forms.CharField(widget=forms.Textarea(attrs={"rows": 3,"placeholder":"Recipe/Dish Description"}))
    class Meta:
        model= Recipe
        fields=['name','description','directions']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # django-crispy-forms
        for field in self.fields:
            new_data = {
                "placeholder": f'Recipe {str(field)}',
                "class": 'form-control',
                #  "hx-post": ".",
                #  "hx-trigger": "keyup changed delay:500ms",
                #  "hx-target": "#recipe-container",
                #  "hx-swap": "outerHTML"
            }
            self.fields[str(field)].widget.attrs.update(
                new_data
            )
        # self.fields['name'].label = ''
        # self.fields['name'].widget.attrs.update({'class': 'form-control-2'})
        self.fields['description'].widget.attrs.update({'rows': '2'})
        self.fields['directions'].widget.attrs.update({'rows': '4'})
        self.fields['name'].help_text='Facing Any Trouble? <a href="/contact">Contact Us</a>'
        


class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['name', 'quantity', 'unit']
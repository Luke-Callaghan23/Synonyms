from django import forms

class Form1 (forms.Form):
    name = forms.CharField (
        label='', 
        initial = 'Bob',
        widget=forms.TextInput (
            attrs={
                'placeholder':'Your name',
            }
        )
    )
    description = forms.CharField (
        initial = 'This is Bob',
        widget=forms.Textarea (
                attrs = {
                "placeholder": "Your description",
                "rows": 20,
                'cols': 120, 
            }
        )
    )
    price = forms.DecimalField(initial=199.99)

    class Meta:
        fields = [
            'name',
            'description',
            'price'
        ]

class Form2 (forms.Form):
    name = forms.CharField (
        label='', 
        initial = 'Joe',
        widget=forms.TextInput (
            attrs={
                'placeholder':'Your name',
            }
        )
    )
    description = forms.CharField (
        initial = 'This is Joe',
        widget=forms.Textarea (
                attrs = {
                "placeholder": "Your description",
                "rows": 20,
                'cols': 120, 
            }
        )
    )
    price = forms.DecimalField(initial=499.99)

    class Meta:
        fields = [
            'name',
            'description',
            'price'
        ]



class SimpleSearchForm (forms.Form):
    class Meta:
        fields = [
            'search_bar'
        ]
    search_bar = forms.CharField (
        required=False,
        label='',
        widget=forms.TextInput (
            attrs={
                'placeholder': 'Search . . . ',
                'class': 'search-item sub-searchbar',
                'style': 'width: 500px'
            }
        ),
        max_length=255
    )
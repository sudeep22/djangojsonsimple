from django import forms


class IndexForm(forms.Form):
    """
        Basic Form with diff-diff fields
    """
    GENDER_CHOICES = [('male', 'Male'), ('female', 'Female')]
    EXPORT_CHOICES = [('json', 'JSON'), ('yaml', 'YAML')]

    export_type = forms.ChoiceField(label='Data Export Type', choices=EXPORT_CHOICES, widget=forms.RadioSelect({
        'class': 'radio-inline',
        'required': 'required'
    }))
    username = forms.CharField(label='Username',
                               widget=forms.TextInput({'maxlength': 10}))
    email = forms.EmailField(label='Email Address')
    name = forms.CharField(label='Full Name')
    gender = forms.ChoiceField(label='Gender', choices=GENDER_CHOICES, widget=forms.RadioSelect({
        'class': 'radio-inline'
    }))
    # number = forms.CharField(label='Phone Number',
    #                          widget=forms.TextInput(attrs={'type':'number'}))
    number = forms.CharField(required=True,
                             widget=forms.TextInput(attrs={'pattern': '[0-9]+', 'maxlength': 10,
                                                           'placeholder': 'Enter your 10 digit phone number'}))
    city = forms.CharField(label='City')

    def __init__(self, *args, **kwargs):
        super(IndexForm, self).__init__(*args, **kwargs)
        form_control_fields = ['username', 'email', 'name', 'number', 'city']
        for field in form_control_fields:
            self.fields[field].widget.attrs.update({
                'class': 'input-md  textinput textInput form-control',
            })

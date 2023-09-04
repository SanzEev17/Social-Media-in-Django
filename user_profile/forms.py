from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_img','bio','age', 'address']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            new_data = {
                'class':'form-control form-control-lg',
                'id': str(field),
                'label':field.capitalize()
            }
            self.fields[str(field)].widget.attrs.update(new_data)
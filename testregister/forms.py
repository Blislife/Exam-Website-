from django import forms

from testregister.models import testDate

class whenTestForm(forms.ModelForm):
    class Meta:
        model = testDate
        fields = ['date']
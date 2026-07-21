from django import forms 
from .models import InstituteProfile

class InstituteForm(forms.ModelForm):
    class Meta:
        model =InstituteProfile
        fields = ["country","address","phone_number","target_line","logo","institute_name"]

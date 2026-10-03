from django import forms
from .models import State, LGA, Ward, PollingUnit
PARTIES = ["PDP","DPP","ACN","PPA","CDC","JP","ANPP","LABOUR","OTHER"]

class PollingUnitResultForm(forms.Form):
    polling_unit = forms.ModelChoiceField(queryset=PollingUnit.objects.all(), label="Polling Unit")

class NewPollingUnitForm(forms.Form):
    state = forms.ModelChoiceField(queryset=State.objects.all())
    lga = forms.ModelChoiceField(queryset=LGA.objects.all())
    ward = forms.ModelChoiceField(queryset=Ward.objects.all())
    uniqueid = forms.IntegerField(min_value=1)
    polling_unit_name = forms.CharField(max_length=255)
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for party in PARTIES:
            self.fields[party] = forms.IntegerField(min_value=0, label=party)
    def clean_uniqueid(self):
        uniqueid = self.cleaned_data["uniqueid"]
        if PollingUnit.objects.filter(uniqueid=uniqueid).exists():
            raise forms.ValidationError("A polling unit with this unique ID already exists.")
        return uniqueid
    def clean(self):
        cleaned = super().clean()
        state, lga, ward = cleaned.get("state"), cleaned.get("lga"), cleaned.get("ward")
        if lga and state and lga.state_id != state.pk:
            self.add_error("lga", "This LGA is not in the selected state.")
        if ward and lga and ward.lga_id != lga.pk:
            self.add_error("ward", "This ward is not in the selected LGA.")
        return cleaned

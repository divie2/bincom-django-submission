from django.contrib import messages
from django.db import transaction
from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect, render
from django import forms
from .forms import PARTIES, PollingUnitResultForm, NewPollingUnitForm
from .models import LGA, PollingUnit, PollingUnitResult

def home(request):
    return render(request, "bincom_app/home.html")

def polling_unit_result(request):
    form = PollingUnitResultForm(request.GET or None)
    result = None
    if form.is_valid():
        pu = form.cleaned_data["polling_unit"]
        rows = PollingUnitResult.objects.filter(polling_unit=pu)
        result = {"polling_unit":pu, "rows":rows, "total":rows.aggregate(t=Sum("score"))["t"] or 0}
    return render(request, "bincom_app/polling_unit.html", {"form":form,"result":result})

def lga_results(request):
    class LGAForm(forms.Form):
        lga = forms.ModelChoiceField(queryset=LGA.objects.all(), required=True)
    form = LGAForm(request.GET or None)
    selected = None
    rows = None
    if form.is_valid():
        selected = form.cleaned_data["lga"]
        rows = (PollingUnitResult.objects.filter(polling_unit__lga=selected)
                .values("party").annotate(total=Sum("score")).order_by("party"))
    return render(request, "bincom_app/lga_results.html", {"form":form,"selected_lga":selected,"rows":rows})

@transaction.atomic
def create_polling_unit(request):
    form = NewPollingUnitForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        pu = PollingUnit.objects.create(
            uniqueid=form.cleaned_data["uniqueid"],
            polling_unit_name=form.cleaned_data["polling_unit_name"],
            ward=form.cleaned_data["ward"],
            lga=form.cleaned_data["lga"],
            state=form.cleaned_data["state"])
        for party in PARTIES:
            PollingUnitResult.objects.create(polling_unit=pu, party=party, score=form.cleaned_data[party])
        messages.success(request, "Polling unit and all party results saved.")
        return redirect("polling_unit_result")
    return render(request, "bincom_app/create_polling_unit.html", {"form":form})

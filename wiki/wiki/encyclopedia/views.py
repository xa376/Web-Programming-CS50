from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django import forms
import markdown2

from . import util

class NewTaskForm(forms.Form):
    formEntry = forms.CharField(label="")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": NewTaskForm()
    })

def entry(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            formEntry = form.cleaned_data["formEntry"]
            if util.get_entry(formEntry):
                return HttpResponseRedirect(formEntry)
            searchMatches = []
            for listEntry in util.list_entries():
                if formEntry.lower() in listEntry.lower():
                    searchMatches.append(listEntry)
            return render(request, "encyclopedia/results.html", {
                "matches": searchMatches
            })

    for listEntry in util.list_entries():
        if listEntry in request.resolver_match:
            return render(request, "encyclopedia/error.html")
            return render(request, "encyclopedia/entry.html", {
                "markdownText": markdown2.markdown(util.get_entry(listEntry))
            })
    
    return render(request, "encyclopedia/entry.html", {
        "testing": request
    })
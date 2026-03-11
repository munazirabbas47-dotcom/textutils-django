# i have created this file /- Abbas
from django.http import HttpResponse
from django.shortcuts import render
import os
from django.conf import settings



def index(request):
    return render(request, "index.html")


def analyze(request):
    # get the text
    djtext = request.POST.get("text", "default")

    # check box values
    removepunc = request.POST.get("removepunc", "off")
    fullcaps = request.POST.get("fullcaps", "off")
    newlinesremover = request.POST.get("newlinesremover", "off")
    extraspaceremover = request.POST.get("extraspaceremover", "off")
    charcounter = request.POST.get("charcounter", "off")

    # check which check box is on
    if removepunc == "on":
        punctuation = """.,?!:;'"'"-_()[]{}/\|@#$%^&*+=<>~`...--___{{}}[[]](())"""
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char
        params = {"purpose": "Remove Punctuation", "analyzed_text": analyzed}
        djtext = analyzed
        

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
            params = {"purpose": "Change to UPPER CASE", "analyzed_text": analyzed}
            djtext = analyzed   
        

    if newlinesremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {"purpose": "Removed NewLine", "analyzed_text": analyzed}
        djtext = analyzed   
        

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {"purpose": "Removed extra space", "analyzed_text": analyzed}
        djtext = analyzed
        

    if charcounter == "on":
        analyzed = f"Length Of Your Text Is: {len(djtext)}"
        params = {"purpose": "Character Counter ", "analyzed_text": analyzed}
        djtext = analyzed   
        


    if removepunc != "on" and fullcaps != "on" and newlinesremover != "on" and extraspaceremover != "on" and charcounter != "on":
        return HttpResponse("Please select any operation and try again.")
    
    
    # render the template
    return render(request, "analyze.html", params)


def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

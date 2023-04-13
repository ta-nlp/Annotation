from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# import spacy
import PyPDF2

# nlp = spacy.load("en_core_web_sm")

def index(request):
    template = loader.get_template('first.html')
    return HttpResponse(template.render({}, request))

def annotate(request):
    x = request.POST['text']
    # doc = nlp(x)
    # html = spacy.displacy.render(doc, style='ent')
    d = {}
    # for ent in doc.ents:
    #     if ent.label_ in d.keys():
    #         d[ent.label_].append(ent.text)
    #     else:
    #         d[ent.label_] = [ent.text]
    # with open('taggingapp/static/data.json', 'w+') as datas:
    #     datas.write(str(d))
    template = loader.get_template('second.html')
    context = {
        'text': x,
        # 'dict': d,
    }
    return HttpResponse(template.render(context, request))

def annotateusingupload(request):
    pdfFileObj = request.FILES['file'] 
    
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    n = pdfReader.numPages
    pageObj = pdfReader.getPage(0)
    x = pageObj.extractText()
    for i in range(n):
        if i != 0:
            pageObj = pdfReader.getPage(i)
            x += pageObj.extractText()
    
    template = loader.get_template('second.html')
    new_string = x.replace("\n", "<br/>" )
    context = {
        'text': new_string,
        # 'dict': d,
    }
    
    return HttpResponse(template.render(context, request))

def help(request):
    template = loader.get_template('help.html')
    return HttpResponse(template.render({}, request))
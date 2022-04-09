from django.shortcuts import render

import pickle
import numpy as np



model=pickle.load(open('./model/covidPrediction.pkl','rb+'))

# Create your views here.
def index(request):
    return render(request, 'home.html')
def covidpage(request):

    return render(request,"covid-test.html")
def result(request):

    BP=int(request.GET['breathing-problem'])
    HP=int(request.GET['hyperTension'])
    FE=int(request.GET['fever'])
    fati=int(request.GET['fatigue'])
    DC=int(request.GET['dry-cough'])
    gas=int(request.GET['gastrointestinal'])
    ST=int(request.GET['Sore-Throat'])
    ABT=int(request.GET['abroad-travel'])
    CLD=int(request.GET['Chronic-Lung-Disease'])
    Head=int(request.GET['Headache'])
    HD=int(request.GET['Heart-Disease'])
    Dia=int(request.GET['Diabetes'])
    VPEA=int(request.GET['Visited-Public-Exposed-Places'])
    FW=int(request.GET['Family-working'])
    WM=int(request.GET['Wearing-Masks'])
    sani=int(request.GET['Sanitization'])
    RN=int(request.GET['Running-Nose'])
    CNW=int(request.GET['contact-with'])
    Asth=int(request.GET['Asthema'])
    AL=int(request.GET['Attended-large'])
    patient=[BP,FE,DC,ST,RN,Asth,CLD,Head,HD,Dia,HP,fati,gas,ABT,CNW,AL,VPEA,FW,WM,sani]
    patient=np.array([patient])
    pred=model.predict(patient)
    if pred[0]==0:
        ans1="You have less chance of Covid-19"
    else:
        ans1="you may have covid-19 take RT PCR test!!"

    context={'ans':ans1}
    return render(request,"result.html",context);
    
def about(request):
    return render(request,"about.html")
def desc(request):
    return render(request,"description.html");
def vaccine(request):
    return render(request,"vaccine.html")            
import pyrebase
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import auth

firebaseConfig = {
    'apiKey': "AIzaSyDKeAyog5zIDCqunVx_UBQbYWaqUEhGHT4",
    'authDomain': "test-project-bcd07.firebaseapp.com",
    'databaseURL': "https://test-project-bcd07.firebaseio.com",
    'projectId': "test-project-bcd07",
    'storageBucket': "test-project-bcd07.appspot.com",
    'messagingSenderId': "411890268348",
    'appId': "1:411890268348:web:b293eab1d31f5ccbaf78b9",
    'measurementId': "G-9HZC5PJ3Y9"
}

firebase = pyrebase.initialize_app(firebaseConfig)

authen = firebase.auth()
database = firebase.database()
uid = ''
idTkn = ''


def index(request):
    return render(request, 'index.html')
    # return render(request, 'addDecision.html')
    # return render(request, 'welcomeAdmin.html')


def open_login(request):
    return render(request, 'login.html')


def login(request):
    eml = request.POST.get('email')
    passwrd = request.POST.get('pword')
    global uid
    global idTkn

    try:
        user = authen.sign_in_with_email_and_password(eml, passwrd)
    except BaseException as e:
        print(e)
        return render(request, '404.html', {'err': e})

    uid = user['localId']
    idTkn = user['idToken']

    print(uid)
    admin = database.child('Admins').child(uid).child('Details').child('Name').get().val()
    admin_state = database.child('Admins').child(uid).child('Details').child('Status').get().val()

    if admin:

        if admin_state == 1:
            print(admin, ' can modify texts in CMS')
        else:
            print(admin, ' can modify images in CMS')

        return render(request, 'welcomeAdmin.html', {'name': admin})

    else:
        return render(request, 'nonAdmin.html')


def signup(request):
    return render(request, 'signup.html')


def register(request):
    name = request.POST.get('name')
    eml = request.POST.get('email')
    passwrd = request.POST.get('pword')
    global uid

    try:
        user = authen.create_user_with_email_and_password(eml, passwrd)
    except Exception as e:
        return render(request, '404.html', {'err': e})

    uid = user['localId']
    data = {"Name": name, "Status": '1'}
    database.child('Admins').child(uid).child('Details').set(data)

    return render(request, 'index.html')


def cms(request):
    return render(request, 'addDecision.html')


def add_decision(request):
    global uid
    id = request.POST.get('id')
    speaker = request.POST.get('speaker')
    decision = request.POST.get('decision')

    choiceA = request.POST.get('choiceA')
    attributeA1 = request.POST.get('attributeA1')
    attributeA1_Val = request.POST.get('attributeA1_Val')
    attributeA2 = request.POST.get('attributeA2')
    attributeA2_Val = request.POST.get('attributeA2_Val')
    attributeA3 = request.POST.get('attributeA3')
    attributeA3_Val = request.POST.get('attributeA3_Val')
    outcomeA_Title = request.POST.get('outcomeA_Title')
    outcomeA_Val = request.POST.get('outcomeA_Val')
    outcomeA = request.POST.get('outcomeA')

    choiceB = request.POST.get('choiceB')
    attributeB1 = request.POST.get('attributeB1')
    attributeB1_Val = request.POST.get('attributeB1_Val')
    attributeB2 = request.POST.get('attributeB2')
    attributeB2_Val = request.POST.get('attributeB2_Val')
    attributeB3 = request.POST.get('attributeB3')
    attributeB3_Val = request.POST.get('attributeB3_Val')
    outcomeB_Title = request.POST.get('outcomeB_Title')
    outcomeB_Val = request.POST.get('outcomeB_Val')
    outcomeB = request.POST.get('outcomeB')

    data = {
        "Speaker": speaker, "Decision": decision,
        "Choices": {
            "Choice A": {
                "Choice": choiceA,
                "Attributes": {
                    "AttributeA1": attributeA1, "AttributeA1_Val": attributeA1_Val,
                    "AttributeA2": attributeA2, "AttributeA2_Val": attributeA2_Val,
                    "AttributeA3": attributeA3, "AttributeA3_Val": attributeA3_Val},
                "Outcomes": {
                    "OutcomeA_Title": outcomeA_Title, "OutcomeA_Val": outcomeA_Val, "outcomeA": outcomeA}
            },
            "Choice B": {
                "Choice": choiceB,
                "Attributes": {
                    "AttributeB1": attributeB1, "AttributeB1_Val": attributeB1_Val,
                    "AttributeB2": attributeB2, "AttributeB2_Val": attributeB2_Val,
                    "AttributeB3": attributeB3, "AttributeB3_Val": attributeB3_Val},
                "Outcomes": {
                    "OutcomeB_Title": outcomeB_Title, "OutcomeB_Val": outcomeB_Val, "outcomeB": outcomeB}
            }
        }
    }
    # data = {
    #     "id": id,
    #     "Speaker": speaker,
    #     "Decision": decision,
    #     "ChoiceA": choiceA,
    #     "AttributeA1": attributeA1,
    #     "AttributeA1_Val": attributeA1_Val,
    #     "AttributeA2": attributeA2,
    #     "AttributeA2_Val": attributeA2_Val,
    #     "AttributeA3": attributeA3,
    #     "AttributeA3_Val": attributeA3_Val,
    #     "OutcomeA_Title": outcomeA_Title,
    #     "OutcomeA_Val": outcomeA_Val,
    #     "outcomeA": outcomeA,
    #     "ChoiceB": choiceB,
    #     "AttributeB1": attributeB1,
    #     "AttributeB1_Val": attributeB1_Val,
    #     "AttributeB2": attributeB2,
    #     "AttributeB2_Val": attributeB2_Val,
    #     "AttributeB3": attributeB3,
    #     "AttributeB3_Val": attributeB3_Val,
    #     "OutcomeB_Title": outcomeB_Title,
    #     "OutcomeB_Val": outcomeB_Val,
    #     "outcomeB": outcomeB
    #     }

    admin = database.child('Admins').child(uid).child('Details').child('Name').get().val()
    database.child('Admins').child('Decisions').child(id).set(data)

    return render(request, 'addDecision.html', {'name': admin})


def load_decision(request):
    global idTkn
    global uid

    ids = database.child('Admins').child('Decisions').shallow().get().val()

    lis_id = []
    lis_decis = []
    lis_speaker = []

    lis_cha = []
    lis_aa1 = []
    lis_aa1v = []
    lis_aa2 = []
    lis_aa2v = []
    lis_aa3 = []
    lis_aa3v = []

    lis_chb = []
    lis_ab1 = []
    lis_ab1v = []
    lis_ab2 = []
    lis_ab2v = []
    lis_ab3 = []
    lis_ab3v = []

    for _id in ids:
        lis_id.append(_id)

    lis_id.sort(reverse=False)

    for _id in lis_id:
        decision = database.child('Admins').child('Decisions').child(_id).child('Decision').get().val()
        speaker = database.child('Admins').child('Decisions').child(_id).child('Speaker').get().val()

        choiceA = database.child('Admins').child('Decisions').child(_id).child('Choices').child('Choice A').\
            child('Choice').get().val()
        attributeA1 = database.child('Admins').child('Decisions').child(_id).child('Choices').child('Choice A'). \
            child('Attributes').child('AttributeA1').get().val()
        attributeA1_Val = database.child('Admins').child('Decisions').child(_id).child('Choices').child('Choice A'). \
            child('Attributes').child('AttributeA1_Val').get().val()
        attributeA2 = database.child('Admins').child('Decisions').child(_id).child('Choices').child('Choice A'). \
            child('Attributes').child('AttributeA2').get().val()
        attributeA2_Val = database.child('Admins').child('Decisions').child(_id).child('Choices').child('Choice A'). \
            child('Attributes').child('AttributeA2_Val').get().val()
        attributeA3 = database.child('Admins').child('Decisions').child(_id).child('Choices').child('Choice A'). \
            child('Attributes').child('AttributeA3').get().val()
        attributeA3_Val = database.child('Admins').child('Decisions').child(_id).child('Choices').child('Choice A'). \
            child('Attributes').child('AttributeA3_Val').get().val()

        choiceB = database.child('Admins').child('Decisions').child(_id).child('Choices').child('Choice B'). \
            child('Choice').get().val()
        attributeB1 = database.child('Admins').child('Decisions').child(_id).child('Choices').child('Choice B'). \
            child('Attributes').child('AttributeB1').get().val()
        attributeB1_Val = database.child('Admins').child('Decisions').child(_id).child('Choices').child('Choice B'). \
            child('Attributes').child('AttributeB1_Val').get().val()
        attributeB2 = database.child('Admins').child('Decisions').child(_id).child('Choices').child('Choice B'). \
            child('Attributes').child('AttributeB2').get().val()
        attributeB2_Val = database.child('Admins').child('Decisions').child(_id).child('Choices').child('Choice B'). \
            child('Attributes').child('AttributeB2_Val').get().val()
        attributeB3 = database.child('Admins').child('Decisions').child(_id).child('Choices').child('Choice B'). \
            child('Attributes').child('AttributeB3').get().val()
        attributeB3_Val = database.child('Admins').child('Decisions').child(_id).child('Choices').child('Choice B'). \
            child('Attributes').child('AttributeB3_Val').get().val()

        lis_decis.append(decision)
        lis_speaker.append(speaker)
        lis_cha.append(choiceA)
        lis_aa1.append(attributeA1)
        lis_aa1v.append(attributeA1_Val)
        lis_aa2.append(attributeA2)
        lis_aa2v.append(attributeA2_Val)
        lis_aa3.append(attributeA3)
        lis_aa3v.append(attributeA3_Val)

        lis_chb.append(choiceB)
        lis_ab1.append(attributeB1)
        lis_ab1v.append(attributeB1_Val)
        lis_ab2.append(attributeB2)
        lis_ab2v.append(attributeB2_Val)
        lis_ab3.append(attributeB3)
        lis_ab3v.append(attributeB3_Val)

    # retrived_data = {lis_id, lis_decis, lis_speaker,
    #                  lis_cha, lis_aa1, lis_aa1v, lis_aa2, lis_aa2v, lis_aa3, lis_aa3v,
    #                  lis_chb, lis_ab1, lis_ab1v, lis_ab2, lis_ab2v, lis_ab3, lis_ab3v}

    # print(retrived_data[lis_decis[0]])

    return render(request, 'loadDecision.html', {'lId': lis_id[0]})

    # return render(request, 'loadDecision.html', {'lId': lis_id, 'lD': lis_decis, 'lS': lis_speaker, 'lCA': lis_cha,
    #                                              'lCA1': lis_aa1, 'lCA1V': lis_aa1v, 'lCA2': lis_aa2, 'lCA2V': lis_aa2v,
    #                                              'lCA3': lis_aa3, 'lCA3V': lis_aa3v, 'lCB': lis_chb,
    #                                              'lCB1': lis_ab1, 'lCB1V': lis_ab1v, 'lCB2': lis_ab2, 'lCB2V': lis_ab2v,
    #                                              'lCB3': lis_ab3, 'lCB3V': lis_ab3v})


def show_decision(request):
    pass


def logout(request):
    auth.logout(request)

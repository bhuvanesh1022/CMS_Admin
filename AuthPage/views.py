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
    request.session['uid'] = str(idTkn)

    print(uid)
    admin = database.child('Admins').child(uid).child('Details').child('Name').get().val()
    admin_state = database.child('Admins').child(uid).child('Details').child('Status').get().val()

    if admin:

        if admin_state == 1:
            print(admin, ' can modify texts in CMS')
        else:
            print(admin, ' can modify images in CMS')

        return load_decision(request, admin)
        # return render(request, 'loadDecision.html', {'name': admin})

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
    data = {
        "choices": {
            "0": {
                "choiceText": request.POST.get('choiceA'),
                "attributeEffects": {
                    "0": {
                        "name": request.POST.get('attributeA1'), "type": request.POST.get('attributeA1_Type'),
                        "value": request.POST.get('attributeA1_Val')
                    },
                    "1": {
                        "name": request.POST.get('attributeA2'), "type": request.POST.get('attributeA2_Type'),
                        "value": request.POST.get('attributeA2_Val'),
                    }
                },
                "consequences": {
                    "0": {
                        "consequenceImage": {
                            "description": request.POST.get('conA0des'), "filename": request.POST.get('conA0fn')
                        },
                        "consequenceText": request.POST.get('conA0'),
                        "statEffects": {
                            "0": {
                                "name": request.POST.get('conA0S0n'), "type": request.POST.get('conA0S0t'),
                                "value": request.POST.get('conA0S0v')
                            },
                            # "1": {
                            #     "name": request.POST.get('conA0S1n'), "type": request.POST.get('conA0S1t'),
                            #     "value": request.POST.get('conA0S1v')
                            # },
                            # "2": {
                            #     "name": request.POST.get('conA0S2n'), "type": request.POST.get('conA0S2t'),
                            #     "value": request.POST.get('conA0S2v')
                            # },
                            # "3": {
                            #     "name": request.POST.get('conA0S3n'), "type": request.POST.get('conA0S3t'),
                            #     "value": request.POST.get('conA0S3v')
                            # }
                        }
                    },
                    "1": {
                        "consequenceImage": {
                            "description": request.POST.get('conA1des'), "filename": request.POST.get('conA1fn')
                        },
                        "consequenceText": request.POST.get('conA1'),
                        "statEffects": {
                            "0": {
                                "name": request.POST.get('conA1S0n'), "type": request.POST.get('conA1S0t'),
                                "value": request.POST.get('conA1S0v')
                            },
                            # "1": {
                            #     "name": request.POST.get('conA1S1n'), "type": request.POST.get('conA1S1t'),
                            #     "value": request.POST.get('conA1S1v')
                            # },
                            # "2": {
                            #     "name": request.POST.get('conA1S2n'), "type": request.POST.get('conA1S2t'),
                            #     "value": request.POST.get('conA1S2v')
                            # },
                            # "3": {
                            #     "name": request.POST.get('conA1S3n'), "type": request.POST.get('conA1S3t'),
                            #     "value": request.POST.get('conA1S3v')
                            # }
                        }
                    },
                    "2": {
                        "consequenceImage": {
                            "description": request.POST.get('conA2des'), "filename": request.POST.get('conA2fn')
                        },
                        "consequenceText": request.POST.get('conA2'),
                        "statEffects": {
                            "0": {
                                "name": request.POST.get('conA2S0n'), "type": request.POST.get('conA2S0t'),
                                "value": request.POST.get('conA2S0v')
                            },
                            # "1": {
                            #     "name": request.POST.get('conA2S1n'), "type": request.POST.get('conA2S1t'),
                            #     "value": request.POST.get('conA2S1v')
                            # },
                            # "2": {
                            #     "name": request.POST.get('conA2S2n'), "type": request.POST.get('conA2S2t'),
                            #     "value": request.POST.get('conA2S2v')
                            # },
                            # "3": {
                            #     "name": request.POST.get('conA2S3n'), "type": request.POST.get('conA2S3t'),
                            #     "value": request.POST.get('conA2S3v')
                            # }
                        }
                    },
                    "3": {
                        "consequenceImage": {
                            "description": request.POST.get('conA3des'), "filename": request.POST.get('conA3fn')
                        },
                        "consequenceText": request.POST.get('conA3'),
                        "statEffects": {
                            "0": {
                                "name": request.POST.get('conA3S0n'), "type": request.POST.get('conA3S0t'),
                                "value": request.POST.get('conA3S0v')
                            },
                            # "1": {
                            #     "name": request.POST.get('conA3S1n'), "type": request.POST.get('conA3S1t'),
                            #     "value": request.POST.get('conA3S1v')
                            # },
                            # "2": {
                            #     "name": request.POST.get('conA3S2n'), "type": request.POST.get('conA3S2t'),
                            #     "value": request.POST.get('conA3S2v')
                            # },
                            # "3": {
                            #     "name": request.POST.get('conA3S3n'), "type": request.POST.get('conA3S3t'),
                            #     "value": request.POST.get('conA3S3v')
                            # }
                        }
                    },
                }
            },
            "1": {
                "choiceText": request.POST.get('choiceB'),
                "attributeEffects": {
                    "0": {
                        "name": request.POST.get('attributeB1'), "type": request.POST.get('attributeB1_Type'),
                        "value": request.POST.get('attributeB1_Val')
                    },
                    "1": {
                        "name": request.POST.get('attributeB2'), "type": request.POST.get('attributeB2_Type'),
                        "value": request.POST.get('attributeB2_Val'),
                    }
                },
                "consequences": {
                    "0": {
                        "consequenceImage": {
                            "description": request.POST.get('conB0des'), "filename": request.POST.get('conB0fn')
                        },
                        "consequenceText": request.POST.get('conB0'),
                        "statEffects": {
                            "0": {
                                "name": request.POST.get('conB0S0n'), "type": request.POST.get('conB0S0t'),
                                "value": request.POST.get('conB0S0v')
                            },
                            # "1": {
                            #     "name": request.POST.get('conB0S1n'), "type": request.POST.get('conB0S1t'),
                            #     "value": request.POST.get('conB0S1v')
                            # },
                            # "2": {
                            #     "name": request.POST.get('conB0S2n'), "type": request.POST.get('conB0S2t'),
                            #     "value": request.POST.get('conB0S2v')
                            # },
                            # "3": {
                            #     "name": request.POST.get('conB0S3n'), "type": request.POST.get('conB0S3t'),
                            #     "value": request.POST.get('conB0S3v')
                            # }
                        }
                    },
                    "1": {
                        "consequenceImage": {
                            "description": request.POST.get('conB1des'), "filename": request.POST.get('conB1fn')
                        },
                        "consequenceText": request.POST.get('conB1'),
                        "statEffects": {
                            "0": {
                                "name": request.POST.get('conB1S0n'), "type": request.POST.get('conB1S0t'),
                                "value": request.POST.get('conB1S0v')
                            },
                            # "1": {
                            #     "name": request.POST.get('conB1S1n'), "type": request.POST.get('conB1S1t'),
                            #     "value": request.POST.get('conB1S1v')
                            # },
                            # "2": {
                            #     "name": request.POST.get('conB1S2n'), "type": request.POST.get('conB1S2t'),
                            #     "value": request.POST.get('conB1S2v')
                            # },
                            # "3": {
                            #     "name": request.POST.get('conB1S3n'), "type": request.POST.get('conB1S3t'),
                            #     "value": request.POST.get('conB1S3v')
                            # }
                        }
                    },
                    "2": {
                        "consequenceImage": {
                            "description": request.POST.get('conB2des'), "filename": request.POST.get('conB2fn')
                        },
                        "consequenceText": request.POST.get('conB2'),
                        "statEffects": {
                            "0": {
                                "name": request.POST.get('conB2S0n'), "type": request.POST.get('conB2S0t'),
                                "value": request.POST.get('conB2S0v')
                            },
                            # "1": {
                            #     "name": request.POST.get('conB2S1n'), "type": request.POST.get('conB2S1t'),
                            #     "value": request.POST.get('conB2S1v')
                            # },
                            # "2": {
                            #     "name": request.POST.get('conB2S2n'), "type": request.POST.get('conB2S2t'),
                            #     "value": request.POST.get('conB2S2v')
                            # },
                            # "3": {
                            #     "name": request.POST.get('conB2S3n'), "type": request.POST.get('conB2S3t'),
                            #     "value": request.POST.get('conB2S3v')
                            # }
                        }
                    },
                    "3": {
                        "consequenceImage": {
                            "description": request.POST.get('conB3des'), "filename": request.POST.get('conB3fn')
                        },
                        "consequenceText": request.POST.get('conB3'),
                        "statEffects": {
                            "0": {
                                "name": request.POST.get('conB3S0n'), "type": request.POST.get('conB3S0t'),
                                "value": request.POST.get('conB3S0v')
                            },
                            # "1": {
                            #     "name": request.POST.get('conB3S1n'), "type": request.POST.get('conB3S1t'),
                            #     "value": request.POST.get('conB3S1v')
                            # },
                            # "2": {
                            #     "name": request.POST.get('conB3S2n'), "type": request.POST.get('conB3S2t'),
                            #     "value": request.POST.get('conB3S2v')
                            # },
                            # "3": {
                            #     "name": request.POST.get('conB3S3n'), "type": request.POST.get('conB3S3t'),
                            #     "value": request.POST.get('conB3S3v')
                            # }
                        }
                    },
                }
            }
        },
        "decisionImage": {
            "description": request.POST.get('description'), "filename": request.POST.get('filename')
        },
        "decisionText": request.POST.get('decision'),
        "requirement": {
            "0": {
                "check": {
                    "name": request.POST.get('r0n'), "type": request.POST.get('r0t'), "value": request.POST.get('r0v')
                },
                "checkType": request.POST.get('rct0')
            },
            "1": {
                "check": {
                    "name": request.POST.get('r1n'), "type": request.POST.get('r1t'), "value": request.POST.get('r1v')
                },
                "checkType": request.POST.get('rct1')
            }
        },
        "speakerName": request.POST.get('speaker')
    }
    global uid
    d_id = request.POST.get('id')

    admin = database.child('Admins').child(uid).child('Details').child('Name').get().val()
    database.child('game-data').child('decisions').child(d_id).set(data)

    return render(request, 'addDecision.html', {'name': admin})


def load_decision(request, admin):
    global idTkn
    global uid

    ids = database.child('game-data').child('decisions').shallow().get().val()

    lis_id = []
    lis_dec = []
    lis_speaker = []

    for _id in ids:
        lis_id.append(_id)

    lis_id.sort()
    print(lis_id)

    for _id in lis_id:
        decision = database.child('game-data').child('decisions').child(_id).child('decisionText').get().val()
        lis_dec.append(decision)

    comb_ls = zip(lis_id, lis_dec)
    return render(request, 'loadDecision.html', {'comb_ls': comb_ls, 'name': admin})


def show_decision(request, z):
    _id = z
    decision = database.child('game-data').child('decisions').child(_id).child('decisionText').get().val()
    speaker = database.child('game-data').child('decisions').child(_id).child('speakerName').get().val()
    description = database.child('game-data').child('decisions').child(_id).child('decisionImage'). \
        child('description').get().val()
    filename = database.child('game-data').child('decisions').child(_id).child('decisionImage'). \
        child('filename').get().val()
    choicea = database.child('game-data').child('decisions').child(_id).child('choices').child('0'). \
        child('choiceText').get().val()

    ata1n = database.child('game-data').child('decisions').child(_id).child('choices').child('0'). \
        child('attributeEffects').child('0').child('name').get().val()
    ata1t = database.child('game-data').child('decisions').child(_id).child('choices').child('0'). \
        child('attributeEffects').child('0').child('type').get().val()
    ata1v = database.child('game-data').child('decisions').child(_id).child('choices').child('0'). \
        child('attributeEffects').child('0').child('value').get().val()
    ata2n = database.child('game-data').child('decisions').child(_id).child('choices').child('0'). \
        child('attributeEffects').child('1').child('name').get().val()
    ata2t = database.child('game-data').child('decisions').child(_id).child('choices').child('0'). \
        child('attributeEffects').child('1').child('type').get().val()
    ata2v = database.child('game-data').child('decisions').child(_id).child('choices').child('0'). \
        child('attributeEffects').child('1').child('value').get().val()

    cac0t = database.child('game-data').child('decisions').child(_id).child('choices').child('0'). \
        child('consequences').child('0').child('consequenceText').get().val()
    cac0d = database.child('game-data').child('decisions').child(_id).child('choices').child('0'). \
        child('consequences').child('0').child('consequenceImage').child('description').get().val()
    cac0f = database.child('game-data').child('decisions').child(_id).child('choices').child('0'). \
        child('consequences').child('0').child('consequenceImage').child('filename').get().val()
    cac0s0n = database.child('game-data').child('decisions').child(_id).child('choices').child('0'). \
        child('consequences').child('0').child('statEffects').child('0').child('name').get().val()
    cac0s0t = database.child('game-data').child('decisions').child(_id).child('choices').child('0'). \
        child('consequences').child('0').child('statEffects').child('0').child('type').get().val()
    cac0s0v = database.child('game-data').child('decisions').child(_id).child('choices').child('0'). \
        child('consequences').child('0').child('statEffects').child('0').child('value').get().val()

    cac1t = database.child('game-data').child('decisions').child(_id).child('choices').child('0'). \
        child('consequences').child('1').child('consequenceText').get().val()
    cac1d = database.child('game-data').child('decisions').child(_id).child('choices').child('0'). \
        child('consequences').child('1').child('consequenceImage').child('description').get().val()
    cac1f = database.child('game-data').child('decisions').child(_id).child('choices').child('0'). \
        child('consequences').child('1').child('consequenceImage').child('filename').get().val()
    cac1s0n = database.child('game-data').child('decisions').child(_id).child('choices').child('0'). \
        child('consequences').child('1').child('statEffects').child('0').child('name').get().val()
    cac1s0t = database.child('game-data').child('decisions').child(_id).child('choices').child('0'). \
        child('consequences').child('1').child('statEffects').child('0').child('type').get().val()
    cac1s0v = database.child('game-data').child('decisions').child(_id).child('choices').child('0'). \
        child('consequences').child('1').child('statEffects').child('0').child('value').get().val()

    cac2t = database.child('game-data').child('decisions').child(_id).child('choices').child('0'). \
        child('consequences').child('2').child('consequenceText').get().val()
    cac2d = database.child('game-data').child('decisions').child(_id).child('choices').child('0'). \
        child('consequences').child('2').child('consequenceImage').child('description').get().val()
    cac2f = database.child('game-data').child('decisions').child(_id).child('choices').child('0'). \
        child('consequences').child('2').child('consequenceImage').child('filename').get().val()
    cac2s0n = database.child('game-data').child('decisions').child(_id).child('choices').child('0'). \
        child('consequences').child('2').child('statEffects').child('0').child('name').get().val()
    cac2s0t = database.child('game-data').child('decisions').child(_id).child('choices').child('0'). \
        child('consequences').child('2').child('statEffects').child('0').child('type').get().val()
    cac2s0v = database.child('game-data').child('decisions').child(_id).child('choices').child('0'). \
        child('consequences').child('2').child('statEffects').child('0').child('value').get().val()

    cac3t = database.child('game-data').child('decisions').child(_id).child('choices').child('0'). \
        child('consequences').child('3').child('consequenceText').get().val()
    cac3d = database.child('game-data').child('decisions').child(_id).child('choices').child('0'). \
        child('consequences').child('3').child('consequenceImage').child('description').get().val()
    cac3f = database.child('game-data').child('decisions').child(_id).child('choices').child('0'). \
        child('consequences').child('3').child('consequenceImage').child('filename').get().val()
    cac3s0n = database.child('game-data').child('decisions').child(_id).child('choices').child('0'). \
        child('consequences').child('3').child('statEffects').child('0').child('name').get().val()
    cac3s0t = database.child('game-data').child('decisions').child(_id).child('choices').child('0'). \
        child('consequences').child('3').child('statEffects').child('0').child('type').get().val()
    cac3s0v = database.child('game-data').child('decisions').child(_id).child('choices').child('0'). \
        child('consequences').child('3').child('statEffects').child('0').child('value').get().val()

    choiceb = database.child('game-data').child('decisions').child(_id).child('choices').child('1'). \
        child('choiceText').get().val()

    atb1n = database.child('game-data').child('decisions').child(_id).child('choices').child('1'). \
        child('attributeEffects').child('0').child('name').get().val()
    atb1t = database.child('game-data').child('decisions').child(_id).child('choices').child('1'). \
        child('attributeEffects').child('0').child('type').get().val()
    atb1v = database.child('game-data').child('decisions').child(_id).child('choices').child('1'). \
        child('attributeEffects').child('0').child('value').get().val()
    atb2n = database.child('game-data').child('decisions').child(_id).child('choices').child('1'). \
        child('attributeEffects').child('1').child('name').get().val()
    atb2t = database.child('game-data').child('decisions').child(_id).child('choices').child('1'). \
        child('attributeEffects').child('1').child('type').get().val()
    atb2v = database.child('game-data').child('decisions').child(_id).child('choices').child('1'). \
        child('attributeEffects').child('1').child('value').get().val()

    cbc0t = database.child('game-data').child('decisions').child(_id).child('choices').child('1'). \
        child('consequences').child('0').child('consequenceText').get().val()
    cbc0d = database.child('game-data').child('decisions').child(_id).child('choices').child('1'). \
        child('consequences').child('0').child('consequenceImage').child('description').get().val()
    cbc0f = database.child('game-data').child('decisions').child(_id).child('choices').child('1'). \
        child('consequences').child('0').child('consequenceImage').child('filename').get().val()
    cbc0s0n = database.child('game-data').child('decisions').child(_id).child('choices').child('1'). \
        child('consequences').child('0').child('statEffects').child('0').child('name').get().val()
    cbc0s0t = database.child('game-data').child('decisions').child(_id).child('choices').child('1'). \
        child('consequences').child('0').child('statEffects').child('0').child('type').get().val()
    cbc0s0v = database.child('game-data').child('decisions').child(_id).child('choices').child('1'). \
        child('consequences').child('0').child('statEffects').child('0').child('value').get().val()

    cbc1t = database.child('game-data').child('decisions').child(_id).child('choices').child('1'). \
        child('consequences').child('1').child('consequenceText').get().val()
    cbc1d = database.child('game-data').child('decisions').child(_id).child('choices').child('1'). \
        child('consequences').child('1').child('consequenceImage').child('description').get().val()
    cbc1f = database.child('game-data').child('decisions').child(_id).child('choices').child('1'). \
        child('consequences').child('1').child('consequenceImage').child('filename').get().val()
    cbc1s0n = database.child('game-data').child('decisions').child(_id).child('choices').child('1'). \
        child('consequences').child('1').child('statEffects').child('0').child('name').get().val()
    cbc1s0t = database.child('game-data').child('decisions').child(_id).child('choices').child('1'). \
        child('consequences').child('1').child('statEffects').child('0').child('type').get().val()
    cbc1s0v = database.child('game-data').child('decisions').child(_id).child('choices').child('1'). \
        child('consequences').child('1').child('statEffects').child('0').child('value').get().val()

    cbc2t = database.child('game-data').child('decisions').child(_id).child('choices').child('1'). \
        child('consequences').child('2').child('consequenceText').get().val()
    cbc2d = database.child('game-data').child('decisions').child(_id).child('choices').child('1'). \
        child('consequences').child('2').child('consequenceImage').child('description').get().val()
    cbc2f = database.child('game-data').child('decisions').child(_id).child('choices').child('1'). \
        child('consequences').child('2').child('consequenceImage').child('filename').get().val()
    cbc2s0n = database.child('game-data').child('decisions').child(_id).child('choices').child('1'). \
        child('consequences').child('2').child('statEffects').child('0').child('name').get().val()
    cbc2s0t = database.child('game-data').child('decisions').child(_id).child('choices').child('1'). \
        child('consequences').child('2').child('statEffects').child('0').child('type').get().val()
    cbc2s0v = database.child('game-data').child('decisions').child(_id).child('choices').child('1'). \
        child('consequences').child('2').child('statEffects').child('0').child('value').get().val()

    cbc3t = database.child('game-data').child('decisions').child(_id).child('choices').child('1'). \
        child('consequences').child('3').child('consequenceText').get().val()
    cbc3d = database.child('game-data').child('decisions').child(_id).child('choices').child('1'). \
        child('consequences').child('3').child('consequenceImage').child('description').get().val()
    cbc3f = database.child('game-data').child('decisions').child(_id).child('choices').child('1'). \
        child('consequences').child('3').child('consequenceImage').child('filename').get().val()
    cbc3s0n = database.child('game-data').child('decisions').child(_id).child('choices').child('1'). \
        child('consequences').child('3').child('statEffects').child('0').child('name').get().val()
    cbc3s0t = database.child('game-data').child('decisions').child(_id).child('choices').child('1'). \
        child('consequences').child('3').child('statEffects').child('0').child('type').get().val()
    cbc3s0v = database.child('game-data').child('decisions').child(_id).child('choices').child('1'). \
        child('consequences').child('3').child('statEffects').child('0').child('value').get().val()

    rc0n = database.child('game-data').child('decisions').child(_id).child('requirement').child('0'). \
        child('check').child('name').get().val()
    rc0t = database.child('game-data').child('decisions').child(_id).child('requirement').child('0'). \
        child('check').child('type').get().val()
    rc0v = database.child('game-data').child('decisions').child(_id).child('requirement').child('0'). \
        child('check').child('value').get().val()
    rct0 = database.child('game-data').child('decisions').child(_id).child('requirement').child('0'). \
        child('checkType').get().val()

    rc1n = database.child('game-data').child('decisions').child(_id).child('requirement').child('1'). \
        child('check').child('name').get().val()
    rc1t = database.child('game-data').child('decisions').child(_id).child('requirement').child('1'). \
        child('check').child('type').get().val()
    rc1v = database.child('game-data').child('decisions').child(_id).child('requirement').child('1'). \
        child('check').child('value').get().val()
    rct1 = database.child('game-data').child('decisions').child(_id).child('requirement').child('1'). \
        child('checkType').get().val()

    data = {
        'id': z, 'sp': speaker,
        'dec': decision, 'desc': description, 'fn': filename,
        'ca': choicea, 'aa1n': ata1n, 'aa1t': ata1t, 'aa1v': ata1v, 'aa2n': ata2n, 'aa2t': ata2t, 'aa2v': ata2v,
        'cac0t': cac0t, 'cac0d': cac0d, 'cac0f': cac0f, 'cac0s0n': cac0s0n, 'cac0s0t': cac0s0t, 'cac0s0v': cac0s0v,
        'cac1t': cac1t, 'cac1d': cac1d, 'cac1f': cac1f, 'cac1s0n': cac1s0n, 'cac1s0t': cac1s0t, 'cac1s0v': cac1s0v,
        'cac2t': cac2t, 'cac2d': cac2d, 'cac2f': cac2f, 'cac2s0n': cac2s0n, 'cac2s0t': cac2s0t, 'cac2s0v': cac2s0v,
        'cac3t': cac3t, 'cac3d': cac3d, 'cac3f': cac3f, 'cac3s0n': cac3s0n, 'cac3s0t': cac3s0t, 'cac3s0v': cac3s0v,
        'cb': choiceb, 'ab1n': atb1n, 'ab1t': atb1t, 'ab1v': atb1v, 'ab2n': atb2n, 'ab2t': atb2t, 'ab2v': atb2v,
        'cbc0t': cbc0t, 'cbc0d': cbc0d, 'cbc0f': cbc0f, 'cbc0s0n': cbc0s0n, 'cbc0s0t': cbc0s0t, 'cbc0s0v': cbc0s0v,
        'cbc1t': cbc1t, 'cbc1d': cbc1d, 'cbc1f': cbc1f, 'cbc1s0n': cbc1s0n, 'cbc1s0t': cbc1s0t, 'cbc1s0v': cbc1s0v,
        'cbc2t': cbc2t, 'cbc2d': cbc2d, 'cbc2f': cbc2f, 'cbc2s0n': cbc2s0n, 'cbc2s0t': cbc2s0t, 'cbc2s0v': cbc2s0v,
        'cbc3t': cbc3t, 'cbc3d': cbc3d, 'cbc3f': cbc3f, 'cbc3s0n': cbc3s0n, 'cbc3s0t': cbc3s0t, 'cbc3s0v': cbc3s0v,
        'rc0n': rc0n, 'rc0t': rc0t, 'rc0v': rc0v, 'rct0': rct0, 'rc1n': rc1n, 'rc1t': rc1t, 'rc1v': rc1v, 'rct1': rct1
    }
    return render(request, 'showDecision.html', {'data': data})


def logout(request):
    try:
        del request.session['uid']
    except KeyError:
        pass
    auth.logout(request)
    return render(request, 'index.html')

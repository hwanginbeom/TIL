import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from .models import BbsUserRegister, Bbs


def loginForm(request):
    if request.session.get('user_id'): # property로 접근
        context = {'id':request.session['user_id'], # 이러한 방법도 가능
                   'name': request.session['user_name']}
        return render(request, 'home.html', context)
    return render(request, 'login.html')

def registerForm(request):
    return render(request, 'join.html')

def register(request):
    if request.method == 'POST':
        id = request.POST['id']  # 값을 받아오는 작업
        pwd = request.POST['pwd']
        name = request.POST['name']
        register = BbsUserRegister(user_id=id, user_pwd=pwd, user_name=name)  # 해당 클래스의 형태로 객체를 만드는 작업
        register.save()  # 객체를 model에 저장한다.
    return redirect('loginForm')  # redirect로 url에 이름으로 지정해놓은 loginForm 으로 이동하게 한다.

def login(request):
    if request.method == 'GET':
        return redirect('login')
    elif request.method == 'POST':
        id = request.POST['id']
        pwd = request.POST['pwd']
        user = BbsUserRegister.objects.get(user_id=id, user_pwd=pwd)  # 객체를 가져온다.
        # user = BbsUserRegister.objects.filter(user_id=id, user_pwd=pwd)  # queryset을 가져온다

        print('user result: ', user)
        context = {}
        if user is not None:
            request.session['user_name'] = user.user_name
            request.session['user_id'] = user.user_id

            context['name'] = request.session['user_name']# 이 세션에 심는다. 이 심은걸 context에 바꿔줘야 한다.
            context['id'] = request.session['user_id']# 이 세션에 심는다. 이 심은걸 context에 바꿔줘야 한다.

    return render(request, 'home.html', context)


def logout(request):
    request.session['user_name'] = {}  # 세션테이블을 초가화 하는 작업이다.
    request.session['user_id'] = {}  # 세션테이블을 초가화 하는 작업이다.

    request.session.modified = True
    return redirect('loginForm')


def list(request):
    boards = Bbs.objects.all()
    print('boadrds result-', boards)
    context = {'boards': boards,
               'id': request.session['user_id'],  # 이러한 방법도 가능
               'name': request.session['user_name']
               }
    return render(request, 'list.html', context)


def bbsRegisterForm(request):
    context = {
               'id': request.session['user_id'],  # 이러한 방법도 가능
               'name': request.session['user_name']
               }
    return render(request, 'bbsRegisterForm.html', context)


def bbsRegister(request):
    if request.method == 'GET':
        return redirect('bbs_registerForm')
    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        writer = request.POST['writer']
        board = Bbs(title=title, content=content, writer=writer)  # 해당 클래스의 형태로 객체를 만드는 작업
        board.save()  # 객체를 model에 저장한다.

        return redirect('bbs_list')  # render로 할 경우에 데이터를 가져올 수가 없다. 그래서 redirect로 한다.


def bbsRead(request,id):
    # id = request.GET['id']
    board = Bbs.objects.get(id=id)  # 객체를 가져온다.
    board.viewcnt = board.viewcnt + 1  # view count 부분이다.
    board.save()
    context = {}
    if board is not None:

        context = {
            'id': request.session['user_id'],  # 이러한 방법도 가능
            'name': request.session['user_name'],
            'board' : board
        }

    print('param - ', board.writer)
    print( id)
    return render(request, 'read.html', context)


def bbsRemove(request):
    id = request.POST['id']
    Bbs.objects.get(id=id).delete()

    return redirect('bbs_list')  # render로 할 경우에 데이터를 가져올 수가 없다. 그래서 redirect로 한다.


def bbsModifyForm(request):
    id = request.POST['id']
    board = Bbs.objects.get(id=id)  # 객체를 가져온다.
    context = {
        'id': request.session['user_id'],  # 이러한 방법도 가능
        'name': request.session['user_name'],
        'board': board
    }

    return render(request, 'modify.html', context)



def bbsModify(request):
    # id = request.GET['id']
    board = Bbs.objects.get(id=id)  # 객체를 가져온다.

    board.viewcnt = board.viewcnt + 1  # view count 부분이다.
    board.save()
    context = {}
    if board is not None:

        context = {
            'id': request.session['user_id'],  # 이러한 방법도 가능
            'name': request.session['user_name'],
            'board': board
        }

    print('param - ', board.writer)
    print( id)
    return render(request, 'read.html', context)


def bbsModify(request):
    id = request.POST['id']
    board = Bbs.objects.get(id=id)  # 객체를 가져온다.
    board.title = request.POST['title']
    board.content = request.POST['content']
    board.save()  # 객체를 model에 저장한다.

    return redirect('bbs_list')  # render로 할 경우에 데이터를 가져올 수가 없다. 그래서 redirect로 한다.


def bbsSearch(request):
    print('ajax json bbsSearch')
    type = request.POST['type']
    keyword = request.POST['keyword']
    print("type:", type, "| keyword:", keyword)

    # model
    # select * from table where title like '%%'
    if type == 'title':
        boards = Bbs.objects.filter(title__startswith=keyword)
    if type == 'writer':
        boards = Bbs.objects.filter(writer__startswith=keyword)
    print("boards--------" , boards)
    data = []
    for board in boards :
        data.append({
            'id'        : board.id,
            'title'     : board.title,
            'writer'    : board.writer,
            'regdate'   : board.regdate,
            'viewcnt'   : board.viewcnt
        })
    print(data)
    # return HttpResponse(json.dumps(dict), content_type='application/json')
    return JsonResponse(data, safe=False)  #  이 부분은 원래 리스트로 받을수 없는데 이 명령어를 통해 리스트를 통해 받을수 있게 한다.








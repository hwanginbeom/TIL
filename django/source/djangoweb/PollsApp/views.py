from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect # 값이 없으면 404 에러를 나타낸다.
from .models import *
from django.urls import reverse
# Create your views here.


def index(request):

    lists = Question.objects.all()
    context = {'lists': lists}

    return render(request, 'polls/index.html', context)


def choice(request, question_id): # get 방식은 이렇게 값을 받을 수 있다.
    print('param question_id' + str(question_id))
    lists = get_object_or_404(Question, pk=question_id)  # 객체가 존재하지 않을 때 404를 띄우고 아닐 경우 값을 받아와 넘긴다.
            # pk 값이 인덱스 값인 question을 가지고 와서 lists에 넣는다. 여기서는 question 객체가 넘어오고
    print("-"*100)
    print(lists)
    print("-"*100)
    context = {'clist': lists}

    return render(request, 'polls/choice.html', context)


def vote(request):
    context = {}
    print(request)
    choice = request.POST['choice'] # name 값을 받는다. 이 name 안에는 value 가 담겨있다.
    question_id = request.POST['question_id'] # name 값을 받는다. 이 name 안에는 value 가 담겨있다.
    print(choice)
    print(question_id)

    question = get_object_or_404(Question, pk=question_id) # 선택된 question
    checked_choice = question.choice_set.get(pk=choice)  # 선택된 초이스 이건 부모 자식간의 관계가 있을 때 가능하다.
    checked_choice.votes += 1  # choice에 votes 값을 1 올려준다.
    checked_choice.save()  # votes 값을 저장한다.
    request.session['question_id'] = question_id
    return redirect('result') # 매개변수를 넣을 수 없다. redirect로 url로 바로 보낸다.
    # render는 템플릿을 띄우는거고 redirect는 url로 보내는 거다.

    # 단순하게 랜더만하면 투표 된 결과만 가져온다. 우리는 DB에 들어가서 값을 가져오는 작업을 해야한다.
    # return render(request, 'polls/result.html', context)
    # return HttpResponseRedirect(reverse('result', args=( (question.id ))) # 매개변수를 넣을수 있고
    # 보내는데 있어서 중간에 view -> 모델 을 들려 값을 가지고 오는 작업이 필요하다.
    # polls result 라고 명시를 해준다. 중복을  대비해 위와같이 쓸 수도 있다.

def result(request):
    question_id = request.session['question_id']
    print('-------------------------  views.result', str(question_id))
    question = get_object_or_404(Question, pk=question_id) # 선택된 question
    context = {'question' : question} # 연관된 관게가 있으면 부모의 자식을 가져와서 쓰라고 권장한다.
    return render(request, 'polls/result.html', context)

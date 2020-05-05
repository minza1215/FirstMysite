from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Question, Choice

# Create your views here.
def index(request):
    #return HttpResponse("Hello, World.")
    
    #2
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    #context = {
    #    'latest_question_list': latest_question_list,
    #}

    #return HttpResponse(template.render(context, request))
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)
    

def detail(request, question_id):
    #1
    #return HttpResponse("You're looking at question %s." % question_id)

    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does  not exist")
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    return HttpResponse(response % question_id)

def vote(requset, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
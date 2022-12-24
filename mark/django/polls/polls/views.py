from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Question, Choice

#homepage
def index(request):
    all_questions = Question.objects.all()

    context = {"all_questions": all_questions}
    return render(request, "polls/index.html", context)

# display a single question
def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
         
    context ={"question":question}
    
    return render(request, "polls/detail.html", context)

# display result of a poll
def results(request, question_id):
    
    question = get_object_or_404(Question, id=question_id)
    
    context = {"question":question}
    
    return render(request, "polls/results.html", context)

# handle interaction of voting
def vote(request, question_id):
    
    choice_id = request.POST['choice']
    
    choice = get_object_or_404(Choice, id=choice_id)
    
    choice.votes += 1
    
    choice.save()
    
    return redirect('results', question_id=question_id)
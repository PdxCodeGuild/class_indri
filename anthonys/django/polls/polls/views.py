from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question, Choice

#Create your views here.
#Home Page
def index(request):
    # This find every question in that table and assign it to all_questions
    all_questions = Question.objects.all()
    context = {"all_questions":all_questions}
    return render(request, "polls/index.html", context)
    # This joins the questions in the list, turns it into a string and is divided by ,
# Create your views here.


# Display a single question
def detail(request, question_id):

    question = get_object_or_404(Question, id=question_id)


    context = {
        "question": question
    }
    return render(request, "polls/detail.html", context)
    
# Display the results of a poll
def results(request, question_id):
    question = get_object_or_404(Question, id=question_id)

    ctx = {"question": question}

    return render(request, "polls/results.html", ctx)

#Handle interaction of voting
def vote(request, question_id):
    choice_id=request.POST['choice']
    choice = get_object_or_404(Choice, id=choice_id)
    
    choice.votes += 1

    choice.save()

    return HttpResponse(f"This choice has {choice.votes} votes!")

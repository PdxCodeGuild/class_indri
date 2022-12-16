from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question, Choice

# Home page.
def index(request):
  all_questions = Question.objects.all()
  context = {
    'all_questions': all_questions
    }
  return render(request, "polls/index.html", context )


#Display a single question
def detail(request, question_id):
  question = get_object_or_404(Question, id=question_id)
  context= { 'question': question}
  print(question.question_text)
  return render(request, "polls/detail.html", context )


#Display results of poll
def results(request, question_id):
  return HttpResponse(f'You are looking at result for question {question_id}')


#Handles voting interaction
def vote(request, question_id):
  choice_id = request.POST['choice']
  choice = get_object_or_404(Choice, id=choice_id)
  choice .votes += 1
  choice.save()
  return HttpResponse(f'This choice has {choice.votes} votes!')




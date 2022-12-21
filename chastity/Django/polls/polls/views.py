from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Home page
def index(request):
    all_questions = Question.objects.all()
    questions = [question.question_text for question in all_questions]
    return HttpResponse(", ".join(questions))


# Display a single question
def detail(request, question_id):
    return HttpResponse(f"You are looking at a question {question_id}")


# Display the results of the poll
def results(request, question_id):
    return HttpResponse(f"You are looking at the results for {question_id}")


# Handle interaction of voting
def vote(request, question_id):
    return HttpResponse(f"You are voting for question {question_id}")

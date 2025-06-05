from django.shortcuts import render
from .models import Question, Answer, Tag, QuestionTag
# Create your views here.

def index(request):
    
    top_questions = Question.get_top_questions()
    questions = Question.objects.all()
    
    context = {
        'top_questions': top_questions,
        'questions': questions
    } 
    
    return render(request, 'blog/index.html', context)
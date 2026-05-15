from django.shortcuts import render
from django.http import Http404
from .models import Question


def index(request):
   latestquestionlist = Question.objects.order_by("-pubdate")[:5]
   context = {"latestquestionlist": latestquestionlist}
   return render(request, "polls/index.html", context)

def detail(request, questionid):
   try:
      question = Question.objects.get(pk=questionid)
   except Question.DoesNotExist:
      raise Http404("Question does not exist")
   return render(request, "polls/detail.html", {"question": question})

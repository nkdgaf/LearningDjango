from django.db.models import F
from django.shortcuts import get_object_or_404, render
from .models import Choice, Question
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def detail(request, questionid):
   return HttpResponse("You're looking at question %s."% questionid)
print(detail)



def results(request, questionid):
   response = "You're looking at the results of the question %s."
   return HttpResponse(response % questionid)


def vote(request, questionid):
   return HttpResponse("You're voting on question %s." % questionid)


def index(request):
   latestquestionlist = Question.objects.order_by("-pubdate")[:5]
   context = {"latestquestionlist": latestquestionlist}
   return render(request, "polls/index.html", context)

def detail(request, questionid):
   question = get_object_or_404(Question, pk=questionid)
   return render(request, "polls/detail.html", {"question": question})



def vote(request, questionid):
   question = get_object_or_404(Question, pk=questionid)
   try:
      selectedchoice=question.choice_set.get(pk=request.POST["choice"])
   except (KeyError, Choice.DoesNotExist):
      return render(
         request,
         "polls/detail.html",
         {
            "question": question,
            "errormessage": "You didn't select a choice.",
         },
      )
   else:
      selectedchoice.votes = F("votes") + 1
      selectedchoice.save()
      return HttpResponseRedirect(reverse("polls:results", args =(question.id)))
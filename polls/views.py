from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    return HttpResponse("Hello, world.")

# Create your views here.

def detail(request, questionid):
    return HttpResponse("You're looking at question %s." % questionid)

def results(request, questionid):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % questionid)

def vote(request, questionid):
    return HttpResponse("You're voting on question %s. " % questionid)

def index(request):
    latestquestionlist = Question.objects.order_by(" - pubdate")[:5]
    output = ", ".join([q.questiontext for q in latestquestionlist])
    return HttpResponse(output)

def index(request):
    latestquestionlist = Question.objects.order_by("pud_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {"latestquestionlist": latestquestionlist}
    return HttpResponse(template.render(context, request))

from django.db.models import F
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import View, generic
from django.core.serializers.json import DjangoJSONEncoder
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Choice, Question


class IndexView(View):
    def get(self, request):
        all_questions = Question.objects.all()
        data_list = []
        for obj in all_questions:
            data_list.append(model_to_dict(obj))

        response = json.dumps(data_list, cls=DjangoJSONEncoder)
        return HttpResponse(response, content_type='application/json')

class DetailView(View):
    def get(self, request, pk):
        question_with_choice = get_object_or_404(Question.objects.prefetch_related('choice_set'), pk=pk)
        choices = list(question_with_choice.choice_set.all().values('id', 'choice_text'))

        question_dict = model_to_dict(question_with_choice)
        question_dict['polls_choice'] = choices

        response = json.dumps(question_dict, cls=DjangoJSONEncoder)
        return HttpResponse(response, content_type='application/json')
    


class ResultsView(generic.DetailView):
    def get(self, request, pk):
        question_with_choice = get_object_or_404(Question.objects.prefetch_related('choice_set'), pk=pk)
        choices = list(question_with_choice.choice_set.all().values('id', 'choice_text', 'votes'))

        question_dict = model_to_dict(question_with_choice)
        question_dict['polls_choice'] = choices

        response = json.dumps(question_dict, cls=DjangoJSONEncoder)
        return HttpResponse(response, content_type='application/json')

@csrf_exempt
def vote(request, question_id):
    if request.method == 'POST':
        question = get_object_or_404(Question, pk=question_id)
        try:
            # { "choice_id": 1 }
            data = json.loads(request.body)
            selected_choice = question.choice_set.get(pk=data["choice_id"])
        except (KeyError, Choice.DoesNotExist, json.JSONDecodeError):
            return JsonResponse({"error": "Invalid choice"}, status=400)
        else:
            selected_choice.votes = F("votes") + 1
            selected_choice.save()
            return JsonResponse({"message": "voted"}, status=201)
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'    

# TODO - Finalize template (which may not be needed, since there is no GET)
def vote(request, question_id):
    """
    Returns an html page that allows the user to vote in the poll.
    :param request: http request
    :param question_id: id of the question being voted on
    :return: html form that allows user to vote
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Re-display the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1  # increment the vote count in the database
        selected_choice.save()  # update the database
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a 
        # user hits the Back button. 
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


#~ def ohsnap(request):
    #~ return HttpResponse("This is another page in polls...Oh Snap!")


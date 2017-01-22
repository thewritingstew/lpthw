from django.http import Http404  # won't need once we use get_object_or_404

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Question, Choice


# index view returns a list of questions
def index(request):
    """
    Returns index.html with latest 5 questions
    :param request: http request
    :return: html page
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


# returns the details of a question with a given id
def detail(request, question_id):
    """
    Returns detail.html for question with id question_id
    :param request: http request
    :param question_id: id of question
    :return: html page
    """
    question = get_object_or_404(Question, pk=question_id)
    ## Try Except was used when we weren't using get_object_or_404
    #~ try:
        #~ question = Question.objects.get(pk=question_id)
    #~ except Question.DoesNotExist:
        #~ raise Http404("Question does not exist.")
        
    return render(request, 'polls/detail.html', {'question': question})
    
# TODO - Finalize template
def results(request, question_id):
    """
    Displays the responses to the question with question id question_id.
    :param request: http request
    :param question_id: id of question
    :return: html page
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
    

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


import datetime

from django.utils import timezone
from django.test import TestCase
from django.urls import reverse

from .models import Question, Choice


def create_question(question_text, days):
    """
    Creates a question with the given 'question_text' and published the 
    given number of 'days' offset to now (negative for questions published 
    in the past, positive for questions that have yet to be published).
    :param question_text: text of question
    :param days: signed integer as number of days from now (positive) or 
                 before now (negative) that question will be/was published
    :return: Question object
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)
    
    
def create_choice(question, choice_text, votes=0):
    """
    Creates a choice for a question.
    :param choice_text: words for the choice
    :param question_id: primary key of Question object the choice is 
                        associated with
    :return: Choice object
    """
    return question.choice_set.create(choice_text=choice_text, votes=votes)

class QuestionMethodTests(TestCase):
    
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions whose 
        pub_date is in the future. 
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    
    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() should return False for questions whose 
        pub_date is more than one day in the past.
        """
        time = timezone.now() - datetime.timedelta(days=2)
        past_question = Question(pub_date=time)
        self.assertIs(past_question.was_published_recently(), False)
        
        
    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() should return True for questions whose 
        pub_date is within the last day.
        """
        time = timezone.now() - datetime.timedelta(days=.5)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


class QuestionIndexViewTests(TestCase):
    def test_index_view_with_no_questions(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        
    
    def test_index_view_with_a_past_question(self):
        """
        Qustions with a pub_date in the past should be displayed on the 
        index page.
        """
        create_question(question_text='Past Question Text', days=-30)
        response = self.client.get(reverse('polls:index'))
        #~ self.assertEqual(response.status_code, 200)
        #~ self.assertContains(response, "Past Question Text")
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past Question Text>']
        )
            
        
    def test_index_view_with_a_future_question(self):
        """
        Questions with a pub_date in the future should not be displayed on 
        the index page.
        """
        create_question(question_text='Future question', days=30)
        response = self.client.get(reverse('polls:index'))
        #~ self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])
        
        
    def test_index_view_with_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions 
        should be displayed.
        """
        create_question(question_text='Past Question Only', days=-30)
        create_question(question_text='Future question', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past Question Only>']
        )
        
        
    def test_index_view_with_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        create_question(question_text='Past Question Two', days=-30)
        create_question(question_text='Past Question One', days=-15)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past Question One>', '<Question: Past Question Two>']
        )


class QuestionDetailViewTests(TestCase):
    def test_detail_view_with_a_future_question(self):
        """
        The detail view of a question with a pub_date in the future should 
        return a 404 not found.
        """
        future_question = create_question(question_text='Future question.', days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        
        
    def test_detail_view_with_a_past_question(self):
        """
        The detail view of a question with a pub_date in the past should 
        display the question's text.
        """
        past_question = create_question(question_text='Past question.', days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)


class QuestionResultsViewTests(TestCase):
    def test_results_view_with_a_future_question(self):
        """
        The results view of a question with a pub_date in the future should 
        return a 404 not found.
        """
        future_question = create_question(question_text='Future question.', days=5)
        choice_one = create_choice(future_question, 'Choice one', votes=2)
        choice_two = create_choice(future_question, 'Choice two', votes=4)
        url = reverse('polls:results', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        
        
    def test_results_view_with_a_past_question(self):
        """
        The results view of a question with a pub_date in the past should 
        display the question's choices and the number of votes for each choice.
        """
        past_question = create_question(question_text='Past question.', days=-5)
        choice_one = create_choice(past_question, 'Choice one', votes=4)
        choice_two = create_choice(past_question, 'Choice two', votes=2)
        #~ choice_one.vote = 2
        #~ choice_two.vote = 4
        url = reverse('polls:results', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
        self.assertContains(response, 
                    choice_one.choice_text + ' -- ' + str(choice_one.votes))
        self.assertContains(response, 
                    choice_two.choice_text + ' -- ' + str(choice_two.votes))



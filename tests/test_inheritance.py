import os
import subprocess

from wizard_builder.models import (
    Choice, Conditional, FormQuestion, MultipleChoice, PageBase, QuestionPage,
    SingleLineText,
)

from django.test import TestCase


class InheritanceTest(TestCase):

    def test_question_page_instance(self):
        page = QuestionPage.objects.create()
        SingleLineText.objects.create(page_id=page.id)
        question = FormQuestion.objects.first()
        self.assertIsInstance(question.page, QuestionPage)

    def test_page_form_question_set_instance(self):
        page = QuestionPage.objects.create()
        SingleLineText.objects.create(page_id=page.id)
        question = PageBase.objects.first().formquestion_set.first()
        self.assertIsInstance(question, SingleLineText)

    def test_choice_multiple_choice_instance(self):
        page = QuestionPage.objects.create()
        question = MultipleChoice.objects.create(page_id=page.id)
        Choice.objects.create(question_id=question.id)
        choice = Choice.objects.first()
        self.assertIsInstance(choice.question, MultipleChoice)

    def test_conditional_instance(self):
        page = QuestionPage.objects.create()
        question = MultipleChoice.objects.create(page_id=page.id)
        Conditional.objects.create(question_id=question.id, page_id=page.id)
        condition = Conditional.objects.first()
        self.assertTrue(QuestionPage.objects.first().conditional)
        self.assertIsInstance(condition.question, MultipleChoice)
        self.assertIsInstance(condition.page, QuestionPage)


class DumpdataHackTest(TestCase):

    def setUp(self):
        subprocess.run('''
            echo "from wizard_builder.models import QuestionPage; QuestionPage.objects.create()" | python tests/test_app/manage.py shell
        ''', shell=True)

    def tearDown(self):
        subprocess.run('''
            echo "from wizard_builder.models import QuestionPage; QuestionPage.objects.all().delete()" | python tests/test_app/manage.py shell
        ''', shell=True)

    def test_dumpdata_hack(self):
        subprocess.check_call('''
            python tests/test_app/manage.py dumpdata \
                wizard_builder \
                -o tests/test_app/dump.json \
                --natural-foreign \
                --indent 2
        ''', shell=True)
        subprocess.check_call('''
            python tests/test_app/manage.py loaddata \
                tests/test_app/dump.json
        ''', shell=True)

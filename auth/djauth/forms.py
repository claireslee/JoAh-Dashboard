from django import forms
from .models import *
from turtle import textinput
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import modelformset_factory
from .models import TeacherInquirie
from .models import Announcement
import json

class LoginForm(forms.ModelForm):
    class Meta:
        model = checkLogin
        fields = ['username', 'password']
        widgets = {
            "username":  forms.TextInput(attrs={'placeholder':'','autocomplete': 'off'}), 
            "password": forms.PasswordInput(attrs={'placeholder':'','autocomplete': 'off','data-toggle': 'password'}),
        }
    
class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['teachername', 'topic', 'announcement']
class StudentForm(forms.ModelForm):
     
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'username', 'password', 'grade']
# QuestionFormSet = modelformset_factory(QuesModel, fields=('question', 'op1', 'op2', 'op3', 'op4', 'ans'), extra=1,)

class addQuestionform(ModelForm):
    class Meta:
        model=QuesModel
        fields="__all__"
        # widgets={'test':forms.HiddenInput(),}
        widgets = {
            'ans': forms.Select(choices=[('option1', 'Option 1'), ('option2', 'Option 2'), ('option3', 'Option 3'), ('option4', 'Option 4')])
        }

class HomeForm(forms.Form):
    post = forms.CharField()

class ExamForm(ModelForm):
    class Meta:
        model=Test
        # fields=['title', 'classes', 'number', 'questions']
        fields=['title']
class EditExamForm(forms.ModelForm):
    test = forms.ModelChoiceField(queryset=Test.objects.all(), label='Select Test')
    title = forms.CharField(label='New Title')

    class Meta:
        model = Test
        fields = ['test', 'title']
class EditQuestionForm(forms.ModelForm):
    question = forms.ModelChoiceField(queryset=QuesModel.objects.all(), label='Select Question')
    questionTitle = forms.CharField(label='New Question', required=False)
    op1 = forms.CharField(label='New Option 1', required=False)
    op2 = forms.CharField(label='New Option 2', required=False)
    op3 = forms.CharField(label='New Option 3', required=False)
    op4 = forms.CharField(label='New Option 4', required=False)
    ans = forms.ChoiceField(choices=[('option1', 'Option 1'), ('option2', 'Option 2'), ('option3', 'Option 3'), ('option4', 'Option 4')], required=False)

    class Meta:
        model = QuesModel
        fields = ['question', 'questionTitle', 'op1', 'op2', 'op3', 'op4', 'ans']

    def clean(self):
        cleaned_data = super().clean()
        question_title = cleaned_data.get('questionTitle')
        op1 = cleaned_data.get('op1')
        op2 = cleaned_data.get('op2')
        op3 = cleaned_data.get('op3')
        op4 = cleaned_data.get('op4')
        ans = cleaned_data.get('ans')

        if not any([question_title, op1, op2, op3, op4, ans]):
            raise forms.ValidationError("At least one field must be filled.")

        return cleaned_data

class DeleteExamForm(forms.Form):
    test = forms.ModelChoiceField(queryset=Test.objects.all(), label='Select Test')

class AddQuestionForm(forms.Form):
    question = forms.ModelChoiceField(queryset=Test.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))
    
class DeleteQuestionForm(forms.Form):
    question = forms.ModelChoiceField(queryset=QuesModel.objects.all(), empty_label=None)

class DeleteQuestionFromExamForm(forms.Form):
    question = forms.ModelChoiceField(queryset=QuesModel.objects.all(), empty_label=None)

    def __init__(self, *args, **kwargs):
        exam_id = kwargs.pop('exam_id')
        super(DeleteQuestionFromExamForm, self).__init__(*args, **kwargs)
        # Update the queryset of the question field based on the exam_id
        self.fields['question'].queryset = QuesModel.objects.filter(Exams__id=exam_id)
class HomeForm(forms.Form):
    post = forms.CharField()

class PdfTestForm(forms.ModelForm):
    num_questions = forms.IntegerField(label='Number of Questions')
    pdf = forms.FileField(label='Select a PDF file')
    file_name = forms.CharField(label='Test Name', max_length=100)
    answers = forms.CharField(widget=forms.HiddenInput(), required=False)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['answers'].initial = self.instance.answers

        # Dynamically add the answer fields based on the num_questions value
        num_questions = self['num_questions'].value()
        if num_questions is not None:
            for i in range(int(num_questions)):
                self.fields[f'q{i+1}'] = forms.ChoiceField(
                    label=f'Answer for Question {i+1}',
                    choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')],
                    widget=forms.RadioSelect,
                    required=False
                )

                if self.instance.pk:
                    answer_choices = json.loads(self.instance.answers)
                    answer_value = answer_choices.get(f'q{i+1}')
                    self.fields[f'q{i+1}'].initial = answer_value
        
    def clean_num_questions(self):
        num_questions = self['num_questions'].value()
        if num_questions is None or int(num_questions) <= 0:
            raise forms.ValidationError('Number of questions must be greater than zero.')
        return num_questions

    def clean(self):
        
        print("Starting clean method...")
        cleaned_data = super().clean()
        
        print("set cleaned_data...")
        num_questions = cleaned_data.get('num_questions')
        
        
        
        print(num_questions)
        if num_questions is None:
            raise forms.ValidationError('Number of questions is required.')
        
        answer_choices_json = cleaned_data.get('answers')
        if answer_choices_json:
            answer_choices = json.loads(answer_choices_json)
            print('num_questions:', num_questions)
            print('answer_choices:', answer_choices)

        # Check that there are enough answer choices for the number of questions
        if num_questions and len(answer_choices) < int(num_questions):
            print(num_questions)
            print(answer_choices)
            raise forms.ValidationError('Not enough answer choices for the number of questions.')

        # Retrieve the values of the answer choices
        answers = {}
        for i in range(1, int(num_questions) + 1):
            question_key = f'q{i}'
            answer = answer_choices[question_key]
            if answer not in ['A', 'B', 'C', 'D']:
                
                raise forms.ValidationError(f'Invalid answer choice for question {i}.')
            print("current answer: ", answer)
            answers[question_key] = answer
            
            print("answers: ", answers)
            print("answers[question_key]: ", answers[question_key])
            


        # Convert the answers to a JSON object
        cleaned_data['answers'] = json.dumps(answers)
    

        return cleaned_data
    
    


    class Meta:
        model = PdfTest
        fields = ['num_questions', 'pdf', 'file_name', 'answers']

class StudentPDFTestForm(forms.Form):
    answers = forms.CharField(widget=forms.HiddenInput(), required=False)
            
    def __init__(self, num_questions, real_answers, student_answers, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.num_questions = num_questions
        self.real_answers = real_answers
        self.student_answers = student_answers
        print("real_answers:", real_answers)
        print("studentans:", student_answers)
        print("numq:", num_questions)
        
                    
                    
    def clean(self):
        print("starting clean method...")
        print("self.answers:", self.real_answers)
        cleaned_data = super().clean()
        answers_json = json.loads(self.student_answers)
        print("answers_json:", answers_json)
        if answers_json:
            answers = answers_json
            print('answers:', answers)           
            num_questions = self.num_questions
            print("len(answers):", len(answers))
            if num_questions and len(answers) < int(num_questions):
                print("number of questions:", num_questions)
                print("answersjson", answers_json)
                raise forms.ValidationError('Not enough answer choices for the number of questions.')

            for i in range(1, int(num_questions) + 1):
                question_key = f'q{i}'
                answer = answers.get(question_key)
                if answer not in ['A', 'B', 'C', 'D']:
                    
                    raise forms.ValidationError(f'Invalid answer choice for question {i}.')
                print("current answer: ", answer)
                answers[question_key] = answer

            cleaned_data['answers'] = json.dumps(answers)
            
        return cleaned_data
        
class DeletePDFForm(forms.Form):
    pdftest = forms.ModelChoiceField(queryset=PdfTest.objects.all(), label='Select Test')
    
    
class TeacherInquirieForm(forms.ModelForm):
    class Meta:
        model = TeacherInquirie
        fields = ['inqteacherfirstname', 'inqteacherlastname', 'inqteacheremail', 'inqteachermessage']
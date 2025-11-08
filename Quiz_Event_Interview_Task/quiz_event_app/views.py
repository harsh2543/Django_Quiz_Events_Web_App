from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Quiz, Question, Answer, UserSubmission, UserAnswer, Event

# Home Page
def index(request):
    return render(request, 'index.html')

# Show all quizzes
def quiz_list(request):
    all_quizzes = Quiz.objects.all()
    return render(request, 'quiz_list.html', {'quizzes': all_quizzes})

# Attempt a quiz
def quiz_attempt(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)                     # get quiz
    questions = Question.objects.filter(quiz=quiz)          # get all questions of that quiz

    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        submission = UserSubmission.objects.create(quiz=quiz, user_name=user_name, score=0)

        score = 0
        for question in questions:
            answer_id = request.POST.get(str(question.id))
            if answer_id:
                answer = Answer.objects.get(id=answer_id)
                is_correct = answer.is_correct
                UserAnswer.objects.create(
                    submission=submission,
                    question=question,
                    answer=answer,
                    is_correct=is_correct
                )
                if is_correct:
                    score += 10

        submission.score = score
        submission.save()
        return redirect('result', submission_id=submission.id)

    return render(request, 'quiz_attempt.html', {'quiz': quiz, 'questions': questions})

# Show quiz result
def result(request, submission_id):
    submission = UserSubmission.objects.get(id=submission_id)
    return render(request, 'result.html', {'submission': submission})

# Show all events
def events(request):
    all_events = Event.objects.all().order_by('date')
    return render(request, 'events.html', {'events': all_events})

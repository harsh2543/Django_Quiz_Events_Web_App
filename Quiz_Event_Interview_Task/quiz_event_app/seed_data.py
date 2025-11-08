from .models import Quiz, Question, Answer, Event, UserAnswer, UserSubmission
from django.utils import timezone

def run():
    # --- OPTIONAL DELETE ALL PREVIOUS DATA ---
    # Quiz.objects.all().delete()
    # Question.objects.all().delete()
    # Answer.objects.all().delete()
    # Event.objects.all().delete()
    # UserAnswer.objects.all().delete()
    # UserSubmission.objects.all().delete()

    # --- PYTHON QUIZ ---
    python_quiz, _ = Quiz.objects.get_or_create(
        title="Python Basics",
        description="Test your knowledge of basic Python concepts."
    )

    # --- OPTIONAL UPDATE QUIZ DATA ---
    # python_quiz.title = "Python Language Quiz"
    # python_quiz.description = "Learn and test your Python programming fundamentals."
    # python_quiz.updated_at = timezone.now()
    # python_quiz.save()    

    # --- Optional Delete all python_quiz previous questions ---
    # Question.objects.filter(quiz=python_quiz).delete()

    q1 = Question.objects.create(quiz=python_quiz, text="What is the output of print(2 + 3 * 4)?", question_type="MCQ")
    Answer.objects.create(question=q1, text="20", is_correct=False)
    Answer.objects.create(question=q1, text="14", is_correct=True)
    Answer.objects.create(question=q1, text="24", is_correct=False)
    Answer.objects.create(question=q1, text="9", is_correct=False)

    q2 = Question.objects.create(quiz=python_quiz, text="Which keyword is used to define a function in Python?", question_type="MCQ")
    Answer.objects.create(question=q2, text="def", is_correct=True)
    Answer.objects.create(question=q2, text="function", is_correct=False)
    Answer.objects.create(question=q2, text="lambda", is_correct=False)
    Answer.objects.create(question=q2, text="define", is_correct=False)

    q3 = Question.objects.create(quiz=python_quiz, text="Which of these is a mutable data type?", question_type="MCQ")
    Answer.objects.create(question=q3, text="tuple", is_correct=False)
    Answer.objects.create(question=q3, text="list", is_correct=True)
    Answer.objects.create(question=q3, text="string", is_correct=False)
    Answer.objects.create(question=q3, text="int", is_correct=False)

    q4 = Question.objects.create(quiz=python_quiz, text="What is used to handle exceptions in Python?", question_type="MCQ")
    Answer.objects.create(question=q4, text="try-except", is_correct=True)
    Answer.objects.create(question=q4, text="catch", is_correct=False)
    Answer.objects.create(question=q4, text="error", is_correct=False)
    Answer.objects.create(question=q4, text="if-else", is_correct=False)

    q5 = Question.objects.create(quiz=python_quiz, text="What is the output of print('Hello' * 3)?", question_type="MCQ")
    Answer.objects.create(question=q5, text="HelloHelloHello", is_correct=True)
    Answer.objects.create(question=q5, text="Hello3", is_correct=False)
    Answer.objects.create(question=q5, text="Error", is_correct=False)
    Answer.objects.create(question=q5, text="333", is_correct=False)

    # --- PHP QUIZ ---
    php_quiz, _ = Quiz.objects.get_or_create(
        title="PHP Basics",
        description="Test your knowledge of PHP programming fundamentals."
    )

    # --- OPTIONAL UPDATE QUIZ DATA ---
    # php_quiz.title = "PHP Language Quiz"
    # php_quiz.description = "Learn and test your Php programming fundamentals."
    # php_quiz.updated_at = timezone.now()
    # php_quiz.save()    

    # --- Optional Delete all php_quiz previous questions ---
    # Question.objects.filter(quiz=php_quiz).delete()

    pq1 = Question.objects.create(quiz=php_quiz, text="Which symbol is used to declare a variable in PHP?", question_type="MCQ")
    Answer.objects.create(question=pq1, text="$", is_correct=True)
    Answer.objects.create(question=pq1, text="#", is_correct=False)
    Answer.objects.create(question=pq1, text="@", is_correct=False)
    Answer.objects.create(question=pq1, text="%", is_correct=False)

    pq2 = Question.objects.create(quiz=php_quiz, text="Which function is used to output data to the screen?", question_type="MCQ")
    Answer.objects.create(question=pq2, text="echo", is_correct=True)
    Answer.objects.create(question=pq2, text="print_r", is_correct=False)
    Answer.objects.create(question=pq2, text="console.log", is_correct=False)
    Answer.objects.create(question=pq2, text="printf", is_correct=False)

    pq3 = Question.objects.create(quiz=php_quiz, text="PHP files have which extension?", question_type="MCQ")
    Answer.objects.create(question=pq3, text=".html", is_correct=False)
    Answer.objects.create(question=pq3, text=".php", is_correct=True)
    Answer.objects.create(question=pq3, text=".py", is_correct=False)
    Answer.objects.create(question=pq3, text=".js", is_correct=False)

    pq4 = Question.objects.create(quiz=php_quiz, text="Which of the following is correct to start a PHP block?", question_type="MCQ")
    Answer.objects.create(question=pq4, text="<?php", is_correct=True)
    Answer.objects.create(question=pq4, text="<php>", is_correct=False)
    Answer.objects.create(question=pq4, text="php{", is_correct=False)
    Answer.objects.create(question=pq4, text="start php", is_correct=False)

    pq5 = Question.objects.create(quiz=php_quiz, text="Which function is used to get the length of a string in PHP?", question_type="MCQ")
    Answer.objects.create(question=pq5, text="strlen()", is_correct=True)
    Answer.objects.create(question=pq5, text="length()", is_correct=False)
    Answer.objects.create(question=pq5, text="strcount()", is_correct=False)
    Answer.objects.create(question=pq5, text="count()", is_correct=False)

    # --- JAVA QUIZ ---
    java_quiz, _ = Quiz.objects.get_or_create(
        title="Java Basics",
        description="Test your knowledge of core Java programming."
    )

    # --- OPTIONAL UPDATE QUIZ DATA ---
    # java_quiz.title = "Java Language Quiz"
    # java_quiz.description = "Learn and test your Java programming fundamentals."
    # java_quiz.updated_at = timezone.now()
    # java_quiz.save()    
    
    # --- Optional Delete all java_quiz previous questions ---
    # Question.objects.filter(quiz=java_quiz).delete()

    jq1 = Question.objects.create(quiz=java_quiz, text="Which of the following is not a Java primitive type?", question_type="MCQ")
    Answer.objects.create(question=jq1, text="int", is_correct=False)
    Answer.objects.create(question=jq1, text="String", is_correct=True)
    Answer.objects.create(question=jq1, text="boolean", is_correct=False)
    Answer.objects.create(question=jq1, text="float", is_correct=False)

    jq2 = Question.objects.create(quiz=java_quiz, text="Which keyword is used to inherit a class in Java?", question_type="MCQ")
    Answer.objects.create(question=jq2, text="inherits", is_correct=False)
    Answer.objects.create(question=jq2, text="extends", is_correct=True)
    Answer.objects.create(question=jq2, text="implements", is_correct=False)
    Answer.objects.create(question=jq2, text="super", is_correct=False)

    jq3 = Question.objects.create(quiz=java_quiz, text="Which method is the entry point of any Java program?", question_type="MCQ")
    Answer.objects.create(question=jq3, text="main()", is_correct=True)
    Answer.objects.create(question=jq3, text="start()", is_correct=False)
    Answer.objects.create(question=jq3, text="run()", is_correct=False)
    Answer.objects.create(question=jq3, text="init()", is_correct=False)

    jq4 = Question.objects.create(quiz=java_quiz, text="What is the size of an int variable in Java?", question_type="MCQ")
    Answer.objects.create(question=jq4, text="2 bytes", is_correct=False)
    Answer.objects.create(question=jq4, text="4 bytes", is_correct=True)
    Answer.objects.create(question=jq4, text="8 bytes", is_correct=False)
    Answer.objects.create(question=jq4, text="16 bytes", is_correct=False)

    jq5 = Question.objects.create(quiz=java_quiz, text="Which company originally developed Java?", question_type="MCQ")
    Answer.objects.create(question=jq5, text="Oracle", is_correct=False)
    Answer.objects.create(question=jq5, text="Sun Microsystems", is_correct=True)
    Answer.objects.create(question=jq5, text="Microsoft", is_correct=False)
    Answer.objects.create(question=jq5, text="IBM", is_correct=False)

    # --- EVENTS ---
    Event.objects.create(title="Django Workshop", description="Learn Django basics in one day.", date="2025-11-10", location="Ahmedabad")
    Event.objects.create(title="Hackathon 2025", description="24-hour coding challenge.", date="2025-12-05", location="Mumbai")
    Event.objects.create(title="Tech Conference", description="Talks on AI, Cloud, and Web Development.", date="2026-01-20", location="Bangalore")

    print("Added 3 Quizzes (Python, PHP, Java) and 3 sample Events Successfully!")
    # print("Quiz updated successfully!")

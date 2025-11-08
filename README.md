# Django_Quiz_Events_Web_App

### Quiz & Event Portal 
• A simple Django web app where users can take quizzes, view their results, and see upcoming events.
  Built using Python, Django, SQLite, and styled with HTML + CSS.

### Features
### Quiz Section
• List all available quizzes
• User can start a quiz
• Dynamically load questions and answers
• On submission: calculate score, display results, and save submission Event Section
• Display upcoming events with title, date, and location

### Event Section
• Display upcoming events with title, date, and location

### Frontend
• Clean design using simple HTML + CSS 
• Pages: Home, Quiz List, Quiz Attempt, Result, Events
### *** Note: Because I have not that much knowledge of Tailwind CSS. ***

### Usage
• Home page: links to Quizzes and Events
• Quiz list: shows all quizzes
• Quiz attempt: enter name and answer questions
• Result page: displays user name and score
• Events page: shows upcoming events

### Setup Instructions
### Go Inside Root Folder
• cd Quiz_Event_Interview_Task 
  or 
• right click on folder and select an option 'open in terminal'

### Run Migrations
• python manage.py makemigrations
• python manage.py migrate

### Sample Data
• Sample data is in the 'quiz_event_app' folder and sample data file name 'seed_data.py'  
• Sample data is in the quiz_event_app/seed_data.py 

### Load Sample Data
• python manage.py shell < quiz_event_app/seed_data.py
  or
• python manage.py shell    
• from quiz_event_app.seed_data import run
• run()

### This will add:
• Quizzes: Python, Java, PHP
• Questions: 5 questions per quiz
• Answers: Multiple-choice answers with correct and incorrect options
• Events: Sample upcoming events

### Run the Server
• python manage.py runserver
• Copy the link and open in your browser 

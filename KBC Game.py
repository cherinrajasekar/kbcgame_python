#KBC Game
questions=[
    'Who is the developer of python language?',
    'When did India get independence?',
    'What is the currency in India?',
    'which state does Bangalore belong to?',
    'Which is the latest iphone?',
]
answers=[
    'Guido Van',
    '1947',
    'INR',
    'Karnataka',
    'iphone 12',
]
options=[
    ['Dennis Ritchi','Alan Frank','Guido Van','Albert'],
    ['1947','1948','1950','2000'],
    ['Euros','Pounds','Dollars','INR'],
    ['Rajasthan','Karnataka','West Bengal','Assam'],
    ['iphone SE','iphone 11','iphone 13','iphone 12'],
]

def play_game(username,questions,answers,options):
    print("Hello",username,",Welcome to the KBC game")
    score=0
    for i in range(len(questions)):
            current_question = questions[i]
            correct_answer = answers[i]
            current_question_options = options[i]
            print("Question:",current_question)
            for index,each_option in enumerate(current_question_options):
               print(index + 1, ")", each_option, sep='')
            user_answer_index = int(input("Enter your choice(1,2,3 0r 4):"))
            user_answer = current_question_options[user_answer_index - 1]
            if user_answer == correct_answer:
                print("Correct answer")
                score=score+100
            else:
                print("Wrong answer")
            break

    print("Your final score is:",score)
    return username,score

def view_scores(names_and_scores):
     for name,score in names_and_scores.items():
         print(name,"has scored",score)

def KBC(questions,answers,options):
    names_and_scores = {}
    while True:
        print("Welcome to the KBC game!")
        print("1)Play game\n2)View scores\n3)Exit")
        choice=int(input("Please enter your choice:"))
        username=input("Enter your name:")
        if choice==1:
          username,score=play_game(username,questions,answers,options)
          names_and_scores[username]=score
        elif choice==2:
            view_scores( names_and_scores)
        elif choice==3:
            break
        else:
            print("Your choice is invalid")
KBC(questions,answers,options)
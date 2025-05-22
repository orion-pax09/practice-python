questions = (
    "How many elements are there in the periodic table?: ",
    "How many planets are there in the solar system:? ",
    "Which of the following is the largest country in the world:? ",
    "Who discovered the neutron:? "
)

options = (
    "A. 116  B. 115  C. 118  D. 119",
    "A. 9  B. 7  C. 8  D. 5",
    "A. CHINA  B. RUSSIA  C. USA  D. GERMANY",
    "A. J.J. THOMSON  B. CHADWICK  C. STRAUDINGER  D. MENDLEEV")

answer = ("C","C","B","B")

guesses=[]

score=0

ques_num= 0

for ques_num , question in enumerate(questions):
    print(" --------- ")
    print(question)
    print(options[ques_num])
for option in options[ques_num].split(" "):
    print(option)

guess= input(f"enter guess of question by clicking A,B,C or D").upper()
guesses.append(guess)
if guess==answer[ques_num]:
    print("answer is corret")
    score +=1
else:
    print("wrong answer", [ques_num])

print(f"your final score is : {score}/len{questions}")
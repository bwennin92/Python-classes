import random


name = "Brandon"
question = "Will I be a good enough Software Engineer?"
answer = ''
random_number = random.randint(1,12)
print(random_number)

if name == "":
  print("Question: " +question)
else:
  print(name + " asks: " + question)


if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "Keep trying"
elif random_number == 11:
  answer = "Have you tried googling it?"
elif random_number == 12:
  answer = "Let me ask ChatGPT"
else:
    answer ="Error"

if question == "":
  print("Hey you need to ask the Magic 8-Ball a question or else KABOOM")
else:
  print("Magic 8-Ball's answer: " + answer)

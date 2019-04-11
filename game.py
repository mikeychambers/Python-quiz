questions = [
        ["What sweet food made by bees using nectar from flowers?", "honey"],
        ["Name the school that Harry Potter attended?", "hogwarts"],
        ["Which country is home to the kangaroo?", "australia"],
        ["Which country sent an Armada to attack Britain in 1588?", "spain"],
        ["Saint Patrick is the Patron Saint of which country?", "ireland"],
        ["From what tree do acorns come?", "oak"],
        ["What is the top colour in a rainbow?", "red"],
        ["In the nursery rhyme, who sat on a wall before having a great fall?", "humpty dumpty"],
        ["What is the capital of Germany?", "berlin"],
        ["Where in Scotland is there supposedly a lake monster called Nessie?", "loch ness"] 
]

def game():
    score = 0
    for x in range(len(questions)):
        print(questions[x][0])
        answer = input()
        answer = answer.lower()
        if answer == questions[x][1]:
            score = score+1
            print("Good Job!")
        else:
            print("Nope")
    if score < 7:
        print("You lose!!!", score, "/10")
        retry()
    else:
        print("WINNER!!!!", score, "/10")
        retry()

def retry():
    print("Another try? y/N")
    retry = input()
    if retry == "y":
       game()
    else:
       exit()

game()


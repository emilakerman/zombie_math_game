import random

def check_answer(user_answer, faktor, tabell_val):
    if user_answer == faktor * tabell_val:
        return "correct"
    else:
        return "not correct"


def place_zombie(ending_interval):
    return random.randint(1, ending_interval)


def reset_game():
    return [], [1,1,1,1,1,1,1,1,1,1,1,1], True, []


def last_question_message_check(doors_opened, remaining_questions):
    if doors_opened == 11 and remaining_questions == 1:
        return "Sista frågan nu!"
    else:
        return ""


def unique_question_check(question, list):
    if question not in list:
        return True
    elif question in list:
        return False


questions = [1,1,1,1,1,1,1,1,1,1,1,1] #  Each number just represents a question
doors = []
list_of_products = [] #  Stores copies of "products" to check for duplicate questions

game_start = True
while game_start:
    print("Du är fast i ett hus med zombies.\nSvara på 12 mattefrågor.\nVälj sedan rätt dörr.")
    running = True
    tabell_val = int(input("\nVilken tabell? (2-12): "))
    while running:
        faktor = random.randint(0, 12)
        unique_question = True
        print(last_question_message_check(len(doors), len(questions)))
        while unique_question:
            faktor = random.randint(0, 12)
            full_question = str(f"{faktor} * {tabell_val}")
            if unique_question_check(full_question, list_of_products):
                list_of_products.append(full_question)
                math_answer = int(input(f"{faktor} * {tabell_val} = "))
                unique_question = False
        if len(doors) != 11:
            if check_answer(math_answer, faktor, tabell_val) == "correct":
                door_choice = int(input(f"Snyggt. Du har nu {len(questions)} dörrar att välja bland, vilken tar du? "))
                zombie_location = place_zombie(len(questions))
                if door_choice == zombie_location:
                    print("Å nej! Du tog dörren där zombien var! Du är nu död.")
                    play_again = str(input("\nVill du spela igen? (j/n) "))
                    if play_again == "j":
                        doors, questions, running, list_of_products = reset_game()
                        break
                    else: 
                        running = False
                        game_start = False
                else:
                    print(f"Snyggt jobbat! Zombien var bakom dörr {zombie_location}.")
                    doors.append("opened")
                    questions.remove(1)
                    print(f"Du har öppnat {len(doors)} dörr(ar). {len(questions)} frågor kvar.")
            else:
                print("Fel svar!")
                play_again = str(input("\nVill du spela igen? (j/n) "))
                if play_again == "j":
                    doors, questions, running, list_of_products = reset_game()
                    break 
                else: 
                    running = False
                    game_start = False
        else:
            play_again = str(input("\nWoho, du vann! Vill du spela igen? (j/n) "))
            if play_again == "j":
                doors, questions, running, list_of_products = reset_game()
                break  
            else: 
                running = False
                game_start = False

def birthday_game():
    # Intro and Oath
    print("🎉 Birthday Truth Game 🎉\n")
    print("Well, I know it's your birthday, but I'm using this game to know the truth, so let's get started, sis! 😎")
    print('RULES:')
    print('⚠ FIRST you need to write this: "I swear to tell the truth and nothing but the truth to my sister Eman even if it hurts."')
    oath = input("Please write the oath exactly as shown: ")

    while oath != "I swear to tell the truth and nothing but the truth to my sister Eman even if it hurts":
        print("😏 Oops, you didn’t type it correctly! Make sure of the capitals and spaces unless it won’t work.")
        oath = input("Please write the oath exactly as shown: ")

    print("🎉 Perfect! Let's get started!\n")

    # Question 1
    print("🧐 Q1: Since it's the first question, I’m going to make it easy.")
    print("In order, list who you hate the most to the least, including mom and dad.")
    print("🤫 Don’t worry, your answer will be secret! No in-betweens, and it has to be from 1 to 11, or else you won't complete the game.\n")
    family_hate_list = input("Enter your list (separate names with commas): ")
    print("👀 Let’s see if I guessed it right...")
    # (Hidden guess list)
    print("😜 Oops, my list didn’t match! Just so you know, you won’t be able to see the list, sis 😉")
    print("Next question!\n")

    # Question 2
    print("❓ Q2: Yes or no, there's no in-between, or else you won’t complete the game.")
    regret_UAEU = input("Did you ever regret not going for UAEU? (Yes or No): ")
    if regret_UAEU.lower() == "yes":
        why_regret = input("😏 If yes, why? ")
        print(f"🤔 Interesting... So you regret it because: {why_regret}")
    else:
        why_not_regret = input("😎 If no, why not? ")
        print(f"👌 Good to know! You don’t regret it because: {why_not_regret}")
    print("Next question!\n")

    # Question 3
    print("🍕 Q3: What’s your favorite food?")
    favorite_food = input("Answer: ")
    print(f"Mmm, {favorite_food} sounds delicious! 😋\n")

    # Question 4
    print("🧐 Q4: What's the real reason behind you leaving music, series, movies, and praying before 2 months?")
    print("🤔 Focus before you answer. Did something happen to you (other than your sickness or marks)? Remember, you swore!")
    real_reason = input("Answer: ")
    print(f"🤐 Got it. So, the reason is: {real_reason}\n")

    # Question 5
    print("🎨 Q5: What’s your favorite color?")
    favorite_color = input("Answer: ")
    print(f"Oooh, {favorite_color}! Nice choice! 🌈\n")

    # Question 6
    print("🧸 Q6: Is it true that you threw my bear because it was haram, or because you had a fight with me?")
    bear_reason = input("Answer: ")
    print(f"😲 Aha, so you threw it because: {bear_reason}\n")

    # Question 7
    print("🌍 Q7: What’s your favorite country?")
    favorite_country = input("Answer: ")
    print(f"{favorite_country}? I see, great choice! ✈️\n")

    # Question 8
    print("💧 Q8: What did you mean when you said your heart needs to be washed 40 times?")
    heart_explanation = input("Answer: ")
    print(f"😊 I already knew, but thanks for confirming: {heart_explanation}\n")

    # Question 9
    print("🎤 Q9: Who is your favorite artist (before)?")
    favorite_artist = input("Answer: ")
    print(f"🎶 Oh, I remember when you used to love {favorite_artist}!\n")

    # Fun point: The cleaning argument
    print('🧼 Quick point I want to clear: When you said "You work for a day, and the rest 10 days you don’t clean," you were wrong!')
    print('Actually, I clean for a day and rest for 10 days')
    print("Let’s continue...\n")

    # Heavy questions start!
    print("🔔 Now the remaining questions will be about me, so get ready because it’s about to get heavy! 💪\n")

    # Question 10
    print("😬 Q10: Remember, write the truth even if it hurts. List 10 bad things about me (+ explanations if needed).")
    bad_things = input("Answer: ")
    print(f"😳 Ouch, those hurt a little, but thanks for the honesty: {bad_things}\n")

    # Question 11
    print("💖 Q11: List 15 good things about me (without extra, please).")
    good_things = input("Answer: ")
    print(f"😊 Aww, that makes me happy! Thanks for the kind words: {good_things}\n")

    # Final round of questions about you
    print("💭 Q12: How do you feel having a sister like me?")
    feeling_sister = input("Answer: ")
    print(f"💖 Aww, that’s sweet: {feeling_sister}\n")

    print("🌟 Q13: What’s your favorite thing about me?")
    favorite_thing = input("Answer: ")
    print(f"💫 That’s great to hear! You love this about me: {favorite_thing}\n")

    print("😡 Q14: What’s the most thing you hate about me? + action in proof.")
    hate_thing = input("Answer: ")
    print(f"🤔 Okay, so you hate this about me: {hate_thing}. Noted!\n")

    print("❤️ Q15: What’s the most thing you love about me? Don’t answer if you don’t have one, and don’t lie!")
    love_thing = input("Answer: ")
    if love_thing:
        print(f"💖 Glad to know you love this about me: {love_thing}\n")
    else:
        print("🤷‍♀️ No answer? Okay, I guess I’ll have to win your love!\n")

    # Ending message
    print("🎉 Thanks for playing the Birthday Truth Game, sis! I hope you had fun (and maybe got a little nervous)! 🎉")
    print("No matter what you answered, I love you, and I’m so happy to celebrate your birthday together! 🎂❤️")

birthday_game()
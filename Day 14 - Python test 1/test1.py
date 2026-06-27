secret = 27  
attempts = 0
max_attempts = 5
print("Number Guessing Game")
print(f"You have {max_attempts} attempts.\n")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret:
        print(" Congratulations! You guessed the secret number!")
        break
    else:
        difference = abs(secret - guess)

        if difference > 20:
            print(" 🧊 Ice Cold!")
        elif difference > 10:
            print("🥶 Cold!")
        elif difference > 5:
            print(" 🌡️ Warm!")
        else:
            print("🔥Hot!")

       
        lives = max_attempts - attempts
        print("Lives left: ", end="")
        for i in range(lives):
            print("❤️", end=" ")
        print("\n")

if attempts == max_attempts and guess != secret:
    print(f" Game Over! The secret number was {secret}.")
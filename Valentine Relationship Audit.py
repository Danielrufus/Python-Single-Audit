import random

print("💔 VALENTINE'S DAY RELATIONSHIP AUDIT 💔")
print("Answer honestly... if you dare 😈")
print("----------------------------------------")

score = 0

user_name = input("Enter your name: ").title()

print("\nWhat type of girl do you like?")
print("1. Cute & Innocent")
print("2. Attitude Queen")
print("3. Gym Girl")
print("4. Rich & Luxury Type")
print("5. Mature & Independent")

girl_choice = input("Choose option (1-5): ")

girl_types = {
    "1": "Cute & Innocent",
    "2": "Attitude Queen",
    "3": "Gym Girl",
    "4": "Rich & Luxury Type",
    "5": "Mature & Independent"
}

girl_type = girl_types.get(girl_choice, "Mystery Type")

print(f"\nAlright {user_name}, you like {girl_type} huh? Interesting 😏")
print("----------------------------------------")

try:
    reply_time = int(input("How many hours do you take to reply to a text? "))
    if reply_time > 2:
        score += 10

    cancel_plans = input("Did you cancel plans to stay home? (yes/no): ").lower()
    if cancel_plans == "yes":
        score += 10

    netflix_time = int(input("How many hours per day do you spend on Netflix/Series? "))
    if netflix_time > 3:
        score += 10

    moved_on = input("Did you fully move on from your ex? (yes/no): ").lower()
    if moved_on == "no":
        score += 15

    last_flirt = int(input("How many months ago did you last flirt with someone? "))
    if last_flirt > 3:
        score += 15

    gym = input("Do you go to gym regularly? (yes/no): ").lower()
    if gym == "no":
        score += 5

    confidence = int(input("Rate your confidence level (1-10): "))
    if confidence < 5:
        score += 10

    balance = float(input("What is your current account balance (₹)? "))
    if balance < 1000:
        score += 20
    elif balance < 5000:
        score += 10
    else:
        score -= 5

except ValueError:
    print("⚠ Invalid input! Please enter numbers only......and proof why you are still single btw")
    exit()

confirm = input("\nBe honest... Did you answer all questions truthfully? (yes/no): ").lower()
if confirm != "yes":
    print("😂 Bro even this audit you are lying. Restart and try again!")
    exit()

single_percentage = min(max(score * 5, 0), 100)

print("\n----------------------------------------")
print(f"💀 {user_name}, Your Single Probability: {single_percentage}%")

if single_percentage > 70:
    print("🔥 Extreme Single Alert!")
elif single_percentage > 40:
    print("😬 Mildly Hopeless Romantic")
else:
    print("😎 You still have hope... maybe.")

roasts = [
    "Even your shadow left you in sunlight 😭",
    "You don’t need a partner, you need character development 📖",
    "Your love life is buffering... forever 📡",
    "Cupid saw you and took leave today 🏹😂",
    "Even spam emails get more attention than your texts 💌",
    "You’re not single by choice... it's by performance 😏",
    "Netflix knows you better than any human 🎬",
    "Your crush calls you 'bro' for a reason 💀",
    "Your bank balance and love balance both low 😂💸",
    "Bro, your account balance is zero… but you're doing emotional investment analysis 💀📉",
    "Bro, the only thing we should be worried about is protein, bro… not pookie girlfriend 💪😂"
]

print("\nSavage Verdict:")
print(random.choice(roasts))

print("\n💘 Based on Your Girl Type Preference:")

if girl_choice == "1":
    print("Cute girls need consistency bro... not mood swings 😭")
elif girl_choice == "2":
    print("Attitude Queen ah? First upgrade your salary package da 💸😂")
elif girl_choice == "3":
    print("Gym girl ah? She lifts heavier standards than your confidence 💪😏")
elif girl_choice == "4":
    print("Luxury type ah? Bro she wants Dubai trips… you and your friends still can’t even plan a beach outing for the past two years💀")
elif girl_choice == "5":
    print("Mature girl ah? She wants stability… not someone defending there football club to haters 😭")
else:
    print("Mystery type ah? Even you don’t know what you want da... just like your career 😂")

if gym == "yes":
    print("\n🏋️ Gym Freak Bonus Roast:")
    print("Focus on protein intake, Buy yourself a whey first. Love can wait 💪😂")

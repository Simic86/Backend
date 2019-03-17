mood_one = "1. happy"
print(mood_one)
mood_two = "2. nervous"
print(mood_two)
mood_three = "3. sad"
print(mood_three)
mood_four = "4. excited"
print(mood_four)
mood_five = "5. relaxed"
print(mood_five)
mood_six = "6. none of the above"
print(mood_six)

mood = int (input ("What is your current mood (enter matching number): "))

if mood == int ("1"):
    print("It is great to see you happy!")
elif mood == int ("2"):
    print("Take a deep breath 3 times.")
elif mood == int ("3"):
    print("Cheer up, mate!")
elif mood == int ("4"):
    print("Yeaah!!")
elif mood == int("5"):
    print ("Keep it cool my friend.")
elif mood == int("6"):
    print("Look deeper :)")
else :
    print("I don't recognize this mood.")



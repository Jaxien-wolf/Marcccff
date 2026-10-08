print("Movie Recommendations")

print("1. Action")
print("2. Comedy")
print("3. Drama")
print("4. Horror")
print("5. Sci-Fi")

Movie = int(input("Pick a genre: "))


if Movie == 1:
    print("Recommended Action Movies: 'Mad Max: Fury Road', 'John Wick', 'Die Hard'")
elif Movie == 2:
    print("Recommended Comedy Movies: 'Superbad', 'The Hangover', 'Step Brothers'")
elif Movie == 3:
    print("Recommended Drama Movies: 'The Shawshank Redemption', 'Forrest Gump', 'The Godfather'")
elif Movie == 4:
    print("Recommended Horror Movies: 'The Conjuring', 'Get Out', 'A Quiet Place'")
elif Movie == 5:
    print("Recommended Sci-Fi Movies: 'Inception', 'Interstellar', 'The Matrix'")
else:
    print("Invalid selection. Please choose a number between 1 and 5.")
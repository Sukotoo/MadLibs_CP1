name = input("Enter a person's name: ")
month = input("Enter a month: ")
day = input("Enter a day: ")
year = input("Enter a year: ")

nouns = [input(f"Enter noun #{i+1}: ") for i in range(5)] # found an awesome way of doing in line for loops
verbs = [input(f"Enter verb #{i+1}: ") for i in range(5)]
adjectives = [input(f"Enter adjective #{i+1}: ") for i in range(3)]
adverbs = [input(f"Enter adverb #{i+1}: ") for i in range(2)]

story_template = (
    f"On {month} {day}, {year}, {name} woke up feeling {adjectives[0]}. "
    f"It was a beautiful day, so they decided to {verbs[0]} with their favorite {nouns[0]}. "
    f"Afterward, {name} found a {adjectives[1]} {nouns[1]} in the middle of the {nouns[2]}. "
    f"Suddenly, the {nouns[3]} began to {verbs[1]} {adverbs[0]}, which startled {name} and made them {verbs[2]} {adverbs[1]}. "
    f"Later in the day, {name} headed to the {nouns[4]} to {verbs[3]}, wearing their most {adjectives[2]} outfit. "
    f"As they {verbs[4]}, they couldn't stop thinking about how strange and exciting the day had been. "
    f"In the end, {name} knew it was a day they would never forget."
)


print(story_template)
print(f"\nAnd they lived {adjectives[2]} ever after!")
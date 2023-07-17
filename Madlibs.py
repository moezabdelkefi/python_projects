with open("story.txt", "r") as f:
    story = f.read()

# Create an empty set to store unique words to be replaced in the story
words = set()
# keep track of the starting index of a word replacement
start_words = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        start_words = i

# Check if the current character is the end of a word replacement
    if char == target_end and start_words != -1:
        word = story[start_words: i + 1]
        words.add(word)
        start_words = -1
# store user provided
answers = {}

for word in words:
    answer = input("enter a word for " + word + ": ")
    answers[word] = answer

# loop each word to set unique words again
for word in words:
    story = story.replace(word, answers[word])
print(story)

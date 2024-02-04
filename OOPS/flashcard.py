class Flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self) -> str:
        return f"{self.word} ({self.meaning})"
    
flash = []
print("Welcome to Flashcard application: ")

while True:
    word = input("Enter the word: ")
    meaning = input("Enter the meaning of the word: ")

    flash.append(Flashcard(word, meaning))
    option = int(input("Enter 0, if you want to add another flashcard: "))

    if option:
        break

# printing all the flashcards 
print("\nYour flashcards")
for i in flash:
    print(">", i)
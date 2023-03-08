import pandas as pd
import random

class Flashcard:
    def __init__(self): 
        try:
            self.language_data = pd.read_csv("data\words_to_learn.csv")
        except FileNotFoundError:
            self.language_data = pd.read_csv("data\\japanese_words.csv")
        self.extract_words = self.language_data.to_dict(orient="records")
        self.random_word = random.choice(self.extract_words)
        self.languages = list(self.random_word.keys())
        self.language_1 = self.languages[0]
        self.language_2 = self.languages[1]
        self.reading = self.languages[2]
        self.label_word = self.random_word[self.language_1]
        self.label_translation = self.random_word[self.language_2]

    def get_word(self):
        self.random_word = random.choice(self.extract_words)
        self.label_word = self.random_word[self.language_1]
        self.label_translation = self.random_word[self.language_2]
        self.read = self.random_word[self.reading]
    
    def save_csv(self):
        self.new_df = pd.DataFrame.from_dict(self.extract_words)
        self.new_df.to_csv("data\words_to_learn.csv", index=False)
        self.language_data = pd.read_csv("data\words_to_learn.csv")

    def remove_word(self):
        self.extract_words.remove(self.random_word)
        self.save_csv()


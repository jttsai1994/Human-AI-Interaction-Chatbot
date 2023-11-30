import spacy
from spacy.training.example import Example
import random

nlp = spacy.blank("en")  # create a blank spaCy model
ner = nlp.add_pipe("ner")
ner.add_label("Moive")
ner.add_label("Date")


# Convert annotated data to spaCy training format
TRAIN_DATA = [
    ("I plan to catch Spider-Man on Monday.", {"entities": [(17, 26, "Movie"), (27, 33, "Date")]}),
    ("This Tuesday, I'm aiming to watch Joker.", {"entities": [(35, 39, "Movie"), (5, 11, "Date")]}),
    ("I'm eager to see Oppenheimer this upcoming Wednesday.", {"entities": [(16, 27, "Movie"), (38, 47, "Date")]}),
    ("Mission Impossible is on my watchlist for this Thursday.", {"entities": [(0, 17, "Movie"), (32, 40, "Date")]}),
    ("The Friday calls for a screening of Spider-Man.", {"entities": [(36, 45, "Movie"), (4, 10, "Date")]}),
    ("I've got Joker lined up for my Saturday movie session.", {"entities": [(9, 13, "Movie"), (32, 39, "Date")]}),
    ("Oppenheimer is the movie I'm eyeing for this Sunday.", {"entities": [(0, 11, "Movie"), (38, 44, "Date")]}),
    ("This Monday, I'm making time for Mission Impossible.", {"entities": [(30, 47, "Movie"), (5, 11, "Date")]}),
    ("Spider-Man is my movie choice for the upcoming Tuesday.", {"entities": [(0, 9, "Movie"), (35, 41, "Date")]}),
    ("I've set aside time to watch Joker this Wednesday.", {"entities": [(28, 32, "Movie"), (43, 52, "Date")]}),
]


train_data_spacy = []
for text, annotations in TRAIN_DATA:
    doc = nlp.make_doc(text)
    example = Example.from_dict(doc, annotations)
    train_data_spacy.append(example)

for epoch in range(25):
    random.shuffle(train_data_spacy)
    losses = {}
    # Update the model with iterating each example
    for example in train_data_spacy:
        nlp.update([example], drop=0.5, losses=losses)
    print(losses)
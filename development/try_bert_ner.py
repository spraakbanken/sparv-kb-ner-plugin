from pprint import pprint

from transformers import pipeline
from tabulate import tabulate

def main():
    nlp = pipeline('ner', model='KBLab/bert-base-swedish-cased-ner', tokenizer='KBLab/bert-base-swedish-cased-ner')

    text = 'Engelbert tar Volvon till Tele2 Arena för att titta på Djurgården IF ' +\
        'som spelar fotboll i VM klockan två på kvällen.'

    tokens = []
    for token in nlp(text):
        if token["word"].startswith("##"):
            tokens[-1]["word"] += token["word"][2:]
        else:
            tokens.append(token)
    # tokens = nlp(text)

    table = ([t["word"], t["score"], t["entity"]] for t in tokens)
    print(tabulate(table, ["word", "score", "entity"]))


if __name__ == "__main__":
    main()

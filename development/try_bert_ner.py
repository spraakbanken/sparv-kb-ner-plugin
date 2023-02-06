from pprint import pprint

from transformers import pipeline
from tabulate import tabulate


def main():
    nlp = pipeline(
        "ner",
        model="KBLab/bert-base-swedish-cased-ner",
        tokenizer="KBLab/bert-base-swedish-cased-ner",
    )

    text = (
        "Engelbert tar Volvon till Tele2 Arena för att titta på Djurgården IF "
        + "som spelar fotboll i VM klockan två på kvällen."
    )

    num_words = len(text.split(" "))
    tokens = []
    for token in nlp(text):
        if token["word"].startswith("##"):
            tokens[-1]["word"] += token["word"][2:]
            tokens[-1]["end"] = token["end"]
        else:
            tokens.append(token)
    # tokens = nlp(text)
    pprint(tokens)
    table = ([t["word"], t["score"], t["entity"], t["index"]] for t in tokens)
    print(tabulate(table, ["word", "score", "entity", "index"]))
    print(f"num words: {num_words}")
    print(f"num tokens: {len(tokens)}")

    tags = []
    end = len(text)
    curr = 0
    curr_token = 0
    while curr < end:
        # print(f"{curr=}, {end=}, {curr_token=}")
        if curr_token < len(tokens) and tokens[curr_token]["start"] == curr:
            print(
                f"word = {tokens[curr_token]['word']}\ttag = {tokens[curr_token]['entity']}"
            )
            curr = tokens[curr_token]["end"]
            curr_token += 1
        else:
            part_end = tokens[curr_token]["start"] if curr_token < len(tokens) else end
            part = text[curr:part_end]
            # print(f"{part=}")
            parts = part.strip().split(" ")
            # print(f"{parts=}")
            for word in parts:
                print(f"word = {word}")
            curr = part_end


if __name__ == "__main__":
    main()

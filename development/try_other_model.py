from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch

tokenizer = AutoTokenizer.from_pretrained(
    "KBLab/bert-base-swedish-lowermix-reallysimple-ner"
)

model = AutoModelForTokenClassification.from_pretrained(
    "KBLab/bert-base-swedish-lowermix-reallysimple-ner"
)
text = [
    "Anna-Lena jobbar för Sveriges Kvinnolobby .".split(),
    "Poliser grep sedan två personer på flygplanet , belarusen Roman Protasevitj och hans flickvän Sofia Sapega .".split(),
]

# text_input = text
text_input = [text[0]]
# [
#     model.config.id2label[t.item()]
#     for t in torch.argmax(
#         model(
#             **tokenizer(text, is_split_into_words=True, return_tensors="pt")
#         ).logits,
#         dim=2,
#     )[0]
# ]


def tokenize_and_align_labels(examples):
    print(f"{type(examples)=}")
    print(f"{type(examples[0])=}")
    print(f"{type(examples[0][0])=}")
    tokenized_inputs = tokenizer(examples, truncation=True, is_split_into_words=True)

    labels = []
    for i, label in enumerate(examples):
        print(f"{i=}, {label=}")
        word_ids = tokenized_inputs.word_ids(
            batch_index=i
        )  # Map tokens to their respective word.
        previous_word_idx = None
        label_ids = []
        for word_idx in word_ids:  # Set the special tokens to -100.
            print(f"{word_idx=}")
            if word_idx is None:
                label_ids.append(-100)
            elif (
                word_idx != previous_word_idx
            ):  # Only label the first token of a given word.
                print(f"{label[word_idx]=}")
                label_ids.append((word_idx, label[word_idx]))
            else:
                print(f"{label[word_idx]=}")
                label_ids.append(-100)
            previous_word_idx = word_idx
        labels.append(label_ids)

    tokenized_inputs["labels"] = labels
    return tokenized_inputs


# tokenize_and_align_labels([text])
# tokenize_and_align_labels([text])["labels"]
# [
#     model.config.id2label[t.item()]
#     for t in torch.argmax(
#         model(
#             **tokenizer([text], is_split_into_words=True, return_tensors="pt")
#         ).logits,
#         dim=2,
#     )[0]
# ]
def run_ner(examples):
    pred = []
    model_out = torch.argmax(
        model(
            **tokenizer(examples, is_split_into_words=True, return_tensors="pt")
        ).logits,
        dim=2,
    )
    for t in model_out:
        print(f"{t=}")
        print(f"{t[0].item()=}")
        pred.append(model.config.id2label[t[0].item()])
    return pred


# pred = [
#     model.config.id2label[t.item()]
#     for t in torch.argmax(
#         model(
#             **tokenizer(text_input, is_split_into_words=True, return_tensors="pt")
#         ).logits,
#         dim=2,
#     )[0]
# ]
pred = run_ner(text_input)
print(f"{pred=}")
print(f"{len(pred)=}")
# print(f"{list(zip(tokenize_and_align_labels([text])['labels'], pred))=}")
# pred_labels = [
#     (t, p)
#     for t, p in zip(tokenize_and_align_labels([text])["labels"], pred)
#     if t != -100
# ]

# print(f"{pred_labels=}")
# # print(f"{pred=}")
# tokenize_and_align_labels([text])["labels"]
tokens = tokenize_and_align_labels(text_input)["labels"][0]
print(f"{tokens=}")
print(f"{len(tokens)=}")
aligned_tokens = [(t, p) for t, p in zip(tokens, pred) if t != -100]
print(f"{aligned_tokens=}")

from transformers import pipeline

generator = pipeline("text-generation", model="distilgpt2")

res = generator(
    "in this course, we will teach you how to",
    max_length = 30, 
    num_return_sequence = 2
)
print(res)
from transformers import T5Tokenizer, T5ForConditionalGeneration
import nltk
import evaluate
import numpy as np
from datasets import load_dataset
from transformers import T5Tokenizer, DataCollatorForSeq2Seq
from transformers import T5ForConditionalGeneration, Seq2SeqTrainingArguments, Seq2SeqTrainer
# Load the tokenizer and model
tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-small")
model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-small")

# Prepare the input text
input_text = "summarize: Your long text goes here."
input_ids = tokenizer(input_text, return_tensors="pt").input_ids

# Generate output
outputs = model.generate(input_ids)

# Decode the output
decoded_output = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(decoded_output)
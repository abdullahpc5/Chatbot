from transformers import GPT2LMHeadModel
from transformers import GPT2Tokenizer

model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

model.eval()

def generate_response(prompt):

    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(inputs, max_length=200, num_return_sequences=1, no_repeat_ngram_size=2)

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response


user_input = "Hello, how are you?"
response = generate_response(user_input)
print("chatbot:", response)
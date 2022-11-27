from transformers import FSMTForConditionalGeneration, FSMTTokenizer

# The Pretrained Transformer Model to use 
mname = "facebook/wmt19-en-de"
# Initialize the tokenizer (preprocessing methods)
tokenizer = FSMTTokenizer.from_pretrained(mname)
# Initialize/download pretrained model
model = FSMTForConditionalGeneration.from_pretrained(mname)

def translate(inputs, model = model, tokenizer=tokenizer):
    # preprocesses a string and returns pytorch tensors
    tokens = tokenizer.encode(inputs, return_tensors="pt")  
    # generate and output with the model
    outputs = model.generate(tokens)
    # Decode the generated tensor and return a human-readable string
    translation = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(inputs, ' : ', translation) 
    return translation

translate("Smash the clap button!")
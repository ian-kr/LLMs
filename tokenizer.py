import re

class TokenizerV1:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {i:s for s,i in vocab.items()}
    
    def encode(self, text):
        preprocessed = re.split(r'([,.?_!"()\']|--|\s)', text)
        preprocessed = [
            item.strip() for item in preprocessed if item.strip()
        ]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids
        
    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)
        return text

with open("frankenstein.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

pre = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)

#print(preprocessed[:20])

all_words = sorted(list(set(pre)))
all_words.extend(["<|endoftext|>", "<|unk|>"])
vocab_size = len(all_words)

vocab = {token:integer for integer, token in enumerate(all_words)}

for i,item in enumerate(list(vocab.items())):
    print(item)

tokenizer = TokenizerV1(vocab)
ids = tokenizer.encode(raw_text)
print(ids)

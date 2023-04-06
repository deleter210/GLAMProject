import torch, sys
sys.path.append('./glam/gpt-neox-20B')
from Tokenizer import GPTNeoXTokenizer
from transformers import GPTNeoXModel, GPTNeoXForCausalLM, GPTNeoXConfig, GPTNeoXLMHeadModel


class GPTNeo:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model_name_or_path = "./glam/gpt-neox-20B"
        self.tokenizer = GPTNeoXTokenizer.from_pretrained(self.model_name_or_path)
        self.model_config = GPTNeoXConfig.from_pretrained(self.model_name_or_path)
        self.model = GPTNeoXLMHeadModel.from_pretrained(self.model_name_or_path, config=self.model_config).to(self.device)
        self.model.eval()
        self.temperature = 0.8
        self.top_p = 0.9
        self.top_k = 0
        self.max_length = 200


    def generate_text(self, prompt="", max_length=100, temperature=0.7, repetition_penalty=1.0, num_return_sequences=1):
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt").to(self.device)
        output_sequences = self.model.generate(
            input_ids=input_ids,
            max_length=max_length + len(input_ids[0]),
            temperature=temperature,
            repetition_penalty=repetition_penalty,
            do_sample=True,
            num_return_sequences=num_return_sequences,
        )
        generated_sequences = []

        for generated_sequence_idx, generated_sequence in enumerate(output_sequences):
            generated_sequence = generated_sequence.tolist()
            text = self.tokenizer.decode(generated_sequence, clean_up_tokenization_spaces=True)
            total_sequence = (
                prompt + text[len(self.tokenizer.decode(input_ids[0], clean_up_tokenization_spaces=True)) :]
            )
            generated_sequences.append(total_sequence)

        return generated_sequences

    def generate_continuation(self, history, prompt="", max_length=100, temperature=0.7, repetition_penalty=1.0, num_return_sequences=1):
        input_ids = self.tokenizer.encode(history + prompt, return_tensors="pt").to(self.device)
        output_sequences = self.model.generate(
            input_ids=input_ids,
            max_length=max_length + len(input_ids[0]),
            temperature=temperature,
            repetition_penalty=repetition_penalty,
            do_sample=True,
            num_return_sequences=num_return_sequences,
        )
        generated_sequences = []

        for generated_sequence_idx, generated_sequence in enumerate(output_sequences):
            generated_sequence = generated_sequence.tolist()
            text = self.tokenizer.decode(generated_sequence, clean_up_tokenization_spaces=True)
            total_sequence = (
                prompt + text[len(self.tokenizer.decode(input_ids[0], clean_up_tokenization_spaces=True)) :]
            )
            generated_sequences.append(total_sequence)

        return generated_sequences


class GPTNeoResponseGenerator:
    def __init__(self):
        self.gpt_neo = GPTNeo()

    def generate_response(self, history, prompt="", max_length=100, temperature=0.7, repetition_penalty=1.0, num_return_sequences=1):
        continuation = self.gpt_neo.generate_continuation(history, prompt=prompt, max_length=max_length, temperature=temperature, repetition_penalty=repetition_penalty, num_return_sequences=num_return_sequences)
        response = continuation[0].split(prompt, 1)[1].strip()
        return response

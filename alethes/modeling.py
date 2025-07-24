"""
Alethes Generator: simple wrapper around a HuggingFace causal LM.
"""
from __future__ import annotations
from dataclasses import dataclass
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

@dataclass
class GenerationConfig:
    model_name_or_path: str = "gpt2"
    max_new_tokens: int = 400
    temperature: float = 0.95
    top_p: float = 0.95

class AlethesGenerator:
    def __init__(self, config: GenerationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.model_name_or_path)
        self.model = AutoModelForCausalLM.from_pretrained(config.model_name_or_path)

    def build_prompt(self, title: str, domain: str, date: str, authors: str) -> str:
        return f"Title: {title}\\nDomain: {domain}\\nDate: {date}\\nAuthors: {authors}\\n\\nArticle:\\n"

    @torch.inference_mode()
    def generate(self, title: str, domain: str, date: str, authors: str) -> str:
        prompt = self.build_prompt(title, domain, date, authors)
        input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids
        out = self.model.generate(
            input_ids,
            max_new_tokens=self.config.max_new_tokens,
            temperature=self.config.temperature,
            top_p=self.config.top_p,
            do_sample=True,
            eos_token_id=self.tokenizer.eos_token_id,
        )
        text = self.tokenizer.decode(out[0], skip_special_tokens=True)
        return text[len(prompt):].strip()

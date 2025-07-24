"""
Alethes Discriminator: wrapper around a HuggingFace sequence classification model.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import List
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

@dataclass
class DiscriminatorConfig:
    model_name_or_path: str = "roberta-base"

class AlethesDiscriminator:
    def __init__(self, config: DiscriminatorConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.model_name_or_path)
        self.model = AutoModelForSequenceClassification.from_pretrained(
            config.model_name_or_path, num_labels=2
        )

    @torch.inference_mode()
    def predict(self, texts: List[str]):
        batch = self.tokenizer(texts, padding=True, truncation=True, return_tensors="pt")
        logits = self.model(**batch).logits
        probs = F.softmax(logits, dim=-1)
        return probs[:, 1].tolist()  # label 1 = synthetic

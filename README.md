# Alethes

**Alethes** (ἀληθές – *truthful* in Greek) is an open-source framework for **synthetic news generation** and **machine-generated news detection**.

Alethes provides:
- **Generator**: produce news-style articles conditioned on metadata (title, date, authors, domain).
- **Discriminator**: classify whether an article is likely synthetic or human-written.

> ⚖️ *Responsible Use:* Alethes can create convincing text. Operators should disclose synthetic content to users and implement rate limiting / logging in production.

## Features

| Component | Description |
|-----------|-------------|
| Generator | Wrapper around a HuggingFace causal language model with metadata prompting. |
| Discriminator | Text classifier (e.g., RoBERTa) producing probability that input is synthetic. |
| CLI Tools | `alethes-generate`, `alethes-detect` for quick usage. |
| Dataset Scripts | Utilities to build a local news dataset for training/evaluation. |

## Installation
```bash
git clone https://github.com/your-org/alethes.git
cd alethes
python -m venv .venv && source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
pip install -e .

Generate an Article
bash
Copy
Edit
python -m alethes.cli.generate \
  --model_name_or_path gpt2 \
  --title "Breakthrough in Battery Technology Slashes Charging Time" \
  --domain technology --date 2025-07-24 --authors "Jane Doe"
Detect Synthetic Text
bash
Copy
Edit
python -m alethes.cli.detect \
  --model_name_or_path roberta-base \
  --input_file examples/articles.jsonl \
  --output_file results/predictions.jsonl
Each output line contains JSON: {"id": "...", "score": 0.83, "is_synthetic": true}.

Project Structure
kotlin
Copy
Edit
alethes/
  alethes/
    generator/
    discriminator/
    cli/
    data/
    utils/
  tests/
Development
bash
Copy
Edit
pip install -r requirements-dev.txt
pytest -q
License
Alethes is licensed under the Apache 2.0 License. See LICENSE and NOTICE for details.

perl
Copy
Edit

Save/commit the file, then say **“done”** and we’ll continue to `requirements.txt`.
::contentReference[oaicite:0]{index=0}

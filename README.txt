# LLM From Scratch

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Status](https://img.shields.io/badge/Project-In%20Progress-orange)
![License](https://img.shields.io/badge/License-MIT-green)

This repository contains my implementation of core components of **Large Language Models (LLMs)** built from scratch for learning and educational purposes.

The goal of this project is to understand how modern language models work internally by implementing each building block step-by-step.

Instead of treating LLMs as black boxes, this project focuses on **building them from first principles**.

---

# Project Overview

Large Language Models such as **GPT, BERT, and LLaMA** consist of several core components.

This repository recreates those components from scratch to understand how they work.
```bash
Raw Text
↓
Tokenizer
↓
Token IDs
↓
Embeddings
↓
Self Attention
↓
Transformer Layers
↓
Language Model
```

---

# Repository Structure
```bash
llm-from-scratch/
│
├── README.md
│
├── notebooks/
│ ├── 01_tokenizer_from_scratch.ipynb
│
├── src/
│ ├── tokenizer.py
│
├── data/
│ └── corpus.txt
│
└── requirements.txt
```


### notebooks

Contains Jupyter notebooks with **step-by-step explanations and experiments**.

### src

Contains **clean Python implementations** of the core components.

### data

Contains text datasets used for vocabulary building and testing.

---

# Implemented Components

## Tokenizer (Regex-Based)

A tokenizer implemented from scratch that:

- splits raw text into tokens using regular expressions
- builds a vocabulary from the dataset
- converts tokens → token IDs
- converts token IDs → text
- handles unknown tokens using a special `<|unk|>` token

### Concepts Covered

- text preprocessing
- tokenization
- vocabulary construction
- encoding and decoding
- special tokens
- handling unknown words

Notebook:
`notebooks/01_tokenizer_from_scratch.ipynb`

---

# Example Usage

```python
from src.tokenizer import SimpleTokenizer

text = "Hello, how are you?"

ids = tokenizer.encode(text)
print(ids)

decoded = tokenizer.decode(ids)
print(decoded)

## Why Build LLM Components From Scratch?

Understanding how LLMs work internally requires knowledge of several components:

- tokenization
- embeddings
- positional encoding
- attention mechanisms
- transformer architectures

By implementing each part manually, we gain a deeper understanding of how models like **GPT** and **BERT** process language.

---

## Upcoming Implementations

This repository will gradually expand to include implementations of:

### Embeddings
- token embeddings
- positional embeddings

### Attention Mechanisms
- scaled dot-product attention
- multi-head attention

### Transformer Architecture
- transformer encoder
- transformer decoder

### Language Model
- mini GPT-style model

---

## Technologies Used

- Python
- NumPy
- Regular Expressions
- Jupyter Notebook

---

## Learning Objectives

This project aims to build intuition for:

- how raw text becomes token IDs
- how tokens are converted into vector representations
- how attention mechanisms work
- how transformers process sequences
- how modern LLM architectures are structured

---

## Future Improvements

Planned improvements include:

- implementing **Byte Pair Encoding (BPE)** tokenizer
- adding **positional embeddings**
- implementing **scaled dot-product attention**
- building a **mini transformer-based language model**
- training a **small GPT-style model**

---

## References

Some resources that inspired this project:

- *Attention Is All You Need* (Vaswani et al.)
- *The Illustrated Transformer*
- GPT architecture papers
- Andrej Karpathy's educational material

---

## Author

**Tarun Rai**

---

⭐ If you find this project useful, consider starring the repository.
# How LLMs Work — Learning Roadmap (Dependency-Based)

## Goal
Provide a structured, first-principles roadmap of how Large Language Models (LLMs) work, including dependencies and prerequisites for each topic.

---

## 1. Problem Framing: Language → Math
**Description:** Computers process numbers, not language. LLMs convert language into mathematical representations.

**Prerequisites:** None

---

## 2. Tokenization (Input Layer)
**Description:** Convert raw text into tokens (smallest units) and map them to integer IDs.

**Prerequisites:**
- Basic understanding of text and strings
- Dictionaries / lookup tables

---

## 3. Embeddings (Representation Layer)
**Description:** Convert tokens into vectors (arrays of numbers) representing meaning.

**Prerequisites:**
- Tokenization
- Basic understanding of arrays/lists
- Intro to vectors

---

## 4. Semantic Space (Meaning Layer)
**Description:** Words are positioned in a high-dimensional space where distance = similarity.

**Prerequisites:**
- Embeddings
- Basic geometry (distance, space)
- Vectors

---

## 5. Vector Relationships (Compositional Meaning)
**Description:** Meaning can be manipulated mathematically (e.g., king - man + woman ≈ queen).

**Prerequisites:**
- Semantic space
- Vector arithmetic (addition/subtraction)

---

## 6. Pre-training (Learning Process)
**Description:** Model learns embeddings by predicting missing/next words across massive datasets.

**Prerequisites:**
- Vector representations
- Basic probability
- Concept of prediction

---

## 7. Sequence Modelling (Context Handling)
**Description:** Understanding how words relate across a sequence (context).

**Prerequisites:**
- Pre-training
- Basic idea of sequences (ordered data)

---

## 8. Transformer Architecture (Core Engine)
**Description:** Mechanism (attention) that allows models to understand relationships across words.

**Prerequisites:**
- Sequence modelling
- Basic matrix operations (optional but helpful)

---

## 9. Inference (Prediction Phase)
**Description:** Model predicts next token based on learned patterns.

**Prerequisites:**
- Transformer architecture
- Probability basics

---

## 10. Sampling & Generation
**Description:** Selecting the next token using probability strategies (top-k, top-p, temperature).

**Prerequisites:**
- Inference
- Probability distributions

---

## 11. Autoregressive Generation Loop
**Description:** Generate text step-by-step by repeatedly predicting the next token.

**Prerequisites:**
- Sampling
- Inference

---

## 12. Model Limitations
**Description:** LLMs do not truly understand; they predict patterns.

**Prerequisites:**
- Inference understanding
- Awareness of training data

---

## 13. Modern Enhancements
**Description:** Techniques improving LLM usefulness (instruction tuning, RLHF, system prompts).

**Prerequisites:**
- Base LLM understanding
- Training vs inference distinction

---

## Recommended Learning Order

1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10 → 11 → 12 → 13

---

## Notes
- Each topic builds on the previous; do not skip levels.
- Focus on intuition first, then dive deeper into math if needed.

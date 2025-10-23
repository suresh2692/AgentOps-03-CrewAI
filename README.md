# Idiomatic Prompt Creator

This project transforms plain human-written text into idiomatic expressions, with the goal of generating diverse and natural-sounding prompts. These prompts can be used to fine-tune language models for more nuanced and expressive output.

## 🌟 Features

- 🔁 Converts plain language into idioms and figurative speech
- 🧠 Useful for generating diverse and high-quality training data
- 📦 Ready to integrate with fine-tuning pipelines (e.g., for LLMs)
- 💡 Enhances creativity and expressiveness in model output

## 🚀 Use Case

You're building a language model and want it to understand or generate idiomatic, non-literal language. This tool helps by transforming straightforward prompts 
like:

`"I’m very happy today."`

into:

`"I'm on cloud nine today."`


These transformed prompts can then be used in datasets for **fine-tuning** or **data augmentation**.

## 🚀 CrewAI Project Setup on macOS (Intel)

Setting up **CrewAI** on an Intel-based Mac can be tricky due to Python and ONNXRuntime compatibility issues.  
Follow these steps to create and run a CrewAI project smoothly.

---

### 1. Create a New CrewAI Project

Use the CrewAI CLI to create a new project:

```bash
crewai create crew <idioms_prompt_creator>
```
### 2. Use Python 3.11 (< 3.12)

CrewAI currently works best with Python 3.11.
Using Python 3.12 may cause onnxruntime errors


### 3. Create a Virtual Environment Using Astral uv
```bash
uv venv
```

### 4. Activate the Virtual Environment

Activate the .venv environment:

```source .venv/bin/activate```

### 5. Run the CrewAI Project

Use uv to run the project inside your environment:

```uv run crewai run```

## AI Models

### Image Generator Models
- Flux **Schnell**: Fastest model for local development & personal use
- Flux **Dev**    : High accuracy than schnell. Distilled version of pro model. 
- **Stable Diffusion 3**
- **Stable Diffusion 1.4**

### Image Captioning
  - **BLIP**
  - **LLaVa 13B**
  - **LLaMA 3.2**

## Tools to download LLMs
- Ollama    (running llms locally)
- llama.cpp (just c++ without pytorch to slow down, runs very fast)
- diffusers & transformers to download models

### App Development stacks
- Langchain (LLM application stack)
- Langserve (LLM serving monitoring)

----

### Running Diffusion Locally
1. Draw Things
2. DiffusionBee
3. Invoke
4. Joyfusion

- Schnell - 12 Billion Parameters
  - Size  : 12 GB
  - 8  bit:  9 GB
----


# Think out aloud: How to build custom Mahabharat Generator
1. First fine-tune
   1. Requires small dataset
   2. Requires small compute
2. ONLY AFTER FINE TUNING - train from scratch
   1. Needs massive datasets
   2. Needs massive compute

# How to fine tune - teach a specific concept to existing model
1. Dreambooth
   1. Teaches a specific concept. (Slows down on large concepts)
   2. More intensive process than LoRA
   3. All parameters of the model are affected
2. LoRA
   1. Teaches a specific concept, by adding small parameters are layer
   2. Only small subset of parameters are updated. 
   3. Faster and scalable than Dreambooth

---
LoRA
- Custom Dataset classes
   - Characters
      - Main Characters
   - Dresses
   - Weapons
      - Bow & Arrow
      - Gada
   - Situations
   - Concepts
      - Hastinapur Castle
      - Graduation ceremony
      - Lakshagruha Castle
      - Draupadi's swyamvar
      - Indra-prastha castle
      - Kurushetra battle
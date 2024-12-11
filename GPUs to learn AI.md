# Big models need GPU
T4 GPU has 15GB VRAM. It falls short
- Llama3.1 8B       -> 16 GB VRAM
- Flux-schnell 12B  -> 24 GB VRAM

Good models start at around 12Billion parameters for both text & images
- 12 Billion Parameter model -> 24 GB VRAM

They all need 24GB GPU. Not available at free tier

# Getting cloud gpu is hard
1. `Google Cloud`. Free tier & GPU quota problem
2. `Replicate`. Easy to use, but credit card problem
3. `Fal.ai`. Just image, doesn't have llm
4. `vast.ai`. Bit complex to navigate
5. Good options
   1. `jarvislabs.ai`. Can recharge with a specific amount. & has Rupees currency
   2. `runpod.io`. Can recharge with specific amount.

# No easy to run script.  
1. replicate makes it easiest to run fine tuning
2. need for standard scripts
3. modular coding + ai assisted coding can help

# Downloading Datasets
1. preprocessing of text datasets is very important, 
   1. text & formatting mistakes are tedious to remove manually
   2. seperate scripts need to be written for each different file
2. 
   1. TODO: should have some llm to do basic preprocessing of text datasets
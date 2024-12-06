Setting up ai-toolkit code, to fine tune
- [x] download & install ai toolkit

Running empty Flux Fine Tuning job, using ai-toolkit
- [x] `config/mahabharat_lora.yaml`
    - adjust 4 values of `training_folder`, `trigger_word`, `datasets.folder_path` , `model.name_or_path`
- [x] run via `python run.py config/mahabharat_on_flux_finetune_lora.yaml`

Captioning images using existing llava model
- [x] generate captions to images using llava model
    - use llava with `transformers` or `ollama` or `llava, lmdeploy` 

- [ ] Download all sub categories of pictures
- [ ] Generate captions of all custom images with llava model
- [ ] edit captions for each to add some specific details. 
- train model on custom dataset
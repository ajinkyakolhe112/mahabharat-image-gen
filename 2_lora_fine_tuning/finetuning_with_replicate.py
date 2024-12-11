import replicate

training = replicate.trainings.create(
  # You need to create a model on Replicate that will be the destination for the trained version.
  destination ="ajinkyakolhe112/MODEL_NAME",
  version     ="ostris/flux-dev-lora-trainer:e440909d3512c31646ee2e0c7d6f6f4923224863a6a10c494606e79fb5844497",
  input={
    "steps": 1000,
    "lora_rank": 16,
    "optimizer": "adamw8bit",
    "batch_size": 1,
    "resolution": "512,768,1024",
    "autocaption": True,
    "input_images": "https://",
    "trigger_word": "TOK",
    "learning_rate": 0.0004,
    "wandb_project": "flux_train_replicate",
    "wandb_save_interval": 100,
    "caption_dropout_rate": 0.05,
    "cache_latents_to_disk": False,
    "wandb_sample_interval": 100
  },
)
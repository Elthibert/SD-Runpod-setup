
import os
import requests
import json

# ... (keep the previous download code) ...

# Define the base path for Stable Diffusion
sd_path = '/workspace/stable-diffusion-webui'

# Define your preferred settings
custom_settings = {
    "sd_model_checkpoint": "PonyRealismV2_1.safetensors",
    "CLIP_stop_at_last_layers": 2,
    "sampler_name": "DPM++ SDE Karras",
    "steps": 35,
    "width": 768,
    "height": 1280,
    "cfg_scale": 7,
    "batch_size": 1,
    "batch_count": 1,
    "seed": -1,
    "refiner_checkpoint": "RealVisXL.safetensors",
    "refiner_switch_at": 0.8,
    "enable_hr": True,
    "hr_upscaler": "1x-ITF-SkinDiffDetail-Lite-v1",
    "hr_second_pass_steps": 35,
    "denoising_strength": 0.4,
    "hr_scale": 2,
    "ad_model": "face_yolov8m.pt,full_eyes_detect_v1.pt",
}

# Create a custom config file
config_path = os.path.join(sd_path, 'config.json')
with open(config_path, 'w') as f:
    json.dump(custom_settings, f, indent=4)

print(f"Custom config saved to {config_path}")

# Create prompt templates
prompts = {
    "positive": "score_9, score_8_up, score_7_up, score_6_up, score_5_up, score_4_up, BREAK,(1girl, 18 years old, freckles),(horny face, horny eyes, horny looking:1.4), blue eyes, intense gaze,(brunette,long hair, eyeliner, blush, lipstick:1.4), amateur, raw, instagram photo, amateur photo, traditional media <lora:AmateurStyle_v1_PONY_REALISM:.3>",
    "negative": "score_1, score_2, score_3, (tattoo:1.5), ink, deformed, deformed face, low quality, bad quality, worst quality, (drawn, furry, illustration, cartoon, anime, comic:1.5), 3d, cgi, extra fingers, (source_anime, source_cartoon, source_furyy, source_western, source_comic, source_pony)",
    "ad_positive1": "(1girl, 18 years old, freckles),(horny face, horny eyes, horny looking:1.4), blue eyes, intense gaze,(brunette,long hair, eyeliner, blush, lipstick:1.4), amateur, raw, instagram photo",
    "ad_negative1": "score_1, score_2, score_3, (tattoo:1.5), ink, deformed, deformed face, low quality, bad quality, worst quality, (drawn, furry, illustration, cartoon, anime, comic:1.5), 3d, cgi, extra fingers, (source_anime, source_cartoon, source_furyy, source_western, source_comic, source_pony)",
    "ad_positive2": "(1girl, 18 years old),blue eyes, raw",
    "ad_negative2": "score_1, score_2, score_3, (tattoo:1.5), ink, deformed, deformed face, low quality, bad quality, worst quality, (drawn, furry, illustration, cartoon, anime, comic:1.5), 3d, cgi, extra fingers, (source_anime, source_cartoon, source_furyy, source_western, source_comic, source_pony)",
}

prompts_path = os.path.join(sd_path, 'prompt_templates.json')
with open(prompts_path, 'w') as f:
    json.dump(prompts, f, indent=4)

print(f"Prompt templates saved to {prompts_path}")

# Modify the launch script
launch_script_path = os.path.join(sd_path, 'webui-user.sh')
launch_command = f"""
export COMMANDLINE_ARGS="--ui-config-file {config_path} --ui-settings-file {config_path} --prompt-templates-file {prompts_path}     --extra-networks-default-multiplier 0.3     --ad-model face_yolov8m.pt --ad-model full_eyes_detect_v1.pt     --ad-conf 0.3 --ad-mask-blur 4 --ad-denoising-strength 0.2 --ad-inpaint-only-masked --ad-use-cfg-scale 4 --ad-use-clip-skip 1     --always-batch-cond-uncond     --no-half-vae"
"""

with open(launch_script_path, 'a') as f:
    f.write(launch_command)

print(f"Launch script updated at {launch_script_path}")

print("Setup complete!")

for prompt in "a word" "two word"
do
  python scripts/txt2img_nonsfw.py --prompt $prompt --plms --outdir Workspace --ddim_steps 100 --ckpt ./models/ldm/stable-diffusion-v1/sd-v1-4-full-ema.ckpt --seed 89
done

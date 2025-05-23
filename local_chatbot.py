
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

model_name = "tiiuae/falcon-7b-instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_name, torch_dtype=torch.float16, trust_remote_code=True, device_map="auto"
)

pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)

def get_sleep_response(user_input):
    prompt = f"""
You are a certified sleep coach AI. Use insights from wearable devices like Fitbit, Apple Health, and clinical research on sleep hygiene, circadian rhythms, and deep sleep. Keep responses practical, kind, and scientific.

Examples:
Q: I wake up tired even after 8 hours. Why?
A: Your sleep quality may be poor — possibly due to limited deep sleep or frequent disturbances. Consider monitoring REM and deep sleep trends using wearable devices.

Q: Is screen time affecting my sleep?
A: Yes. Exposure to blue light before bed can suppress melatonin and disrupt your natural sleep cycle.

Q: {user_input}
A:"""
    result = pipe(prompt, max_new_tokens=200, do_sample=True, temperature=0.7, top_p=0.9)
    return result[0]["generated_text"].split("A:")[-1].strip()

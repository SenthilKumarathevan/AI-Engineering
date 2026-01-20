import openai
from foundry_local import FoundryLocalManager
alias = "qwen2.5-0.5b"
manager = FoundryLocalManagera(alias)
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Set the model to use and generate a streaming response
stream = Client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Why is the sky blue?"}],
    stream=True
)

# Print the streaming response as it arrives
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="", flush=True)

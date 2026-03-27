from openai import OpenAI

client = OpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1"
)

try:
    response = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Hello, are you working?"}
        ]
    )

    print("✅ API is working!")
    print(response.choices[0].message.content)

except Exception as e:
    print("❌ API ERROR:")
    print(e)
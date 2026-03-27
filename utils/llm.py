import os
from openai import OpenAI
from dotenv import load_dotenv

# 🔐 Load environment variables
load_dotenv(dotenv_path=".env", override=True)

# 🔍 Get API key
api_key = os.getenv("OPENROUTER_API_KEY")

# Clean API key
if api_key:
    api_key = api_key.strip().strip('"').strip("'")

# ❌ If missing
if not api_key:
    raise ValueError("❌ OPENROUTER_API_KEY not found. Check your .env file.")

# ✅ Initialize OpenRouter client
client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)


def generate_answer(context, question):
    """
    Final version: complete + accurate + document-only answers
    """

    # 🔒 Safety check
    if not context or len(context.strip()) < 50:
        return "The answer is not available in the document."

    prompt = f"""
Answer the question ONLY using the given document.

Instructions:
- Read the FULL context carefully
- The answer may be long
- Include ALL relevant details
- Do NOT shorten the answer
- Combine information from different parts if needed
- Give a complete and clear answer

STRICT RULES:
- Use ONLY the provided context
- DO NOT use outside knowledge
- DO NOT guess
- DO NOT ask questions back

IMPORTANT:
- If the answer is not found, say exactly:
  "The answer is not available in the document."

Context:
{context}

Question:
{question}
"""

    try:
        response = client.chat.completions.create(
            model="meta-llama/llama-3-8b-instruct",  # ⚡ fast + good quality
            messages=[
                {"role": "system", "content": "You answer strictly from documents."},
                {"role": "user", "content": prompt}
            ],
            temperature=0,
            max_tokens=700   # 🔥 increased for full answers
        )

        answer = response.choices[0].message.content.strip()

        return answer

    except Exception as e:
        return f"❌ Error: {str(e)}"
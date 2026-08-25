# The basic request/response pattern
import anthropic

client = anthropic.Anthropic()  # reads your API key from the environment

message = client.messages.create(
    model="claude-sonnet-5",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Explain what an API is, in one sentence."}
    ]
)

print(message.content[0].text)


# The OpenAI API follows a nearly identical shape:


from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": "Explain what an API is, in one sentence."}
    ]
)

print(response.choices[0].message.content)
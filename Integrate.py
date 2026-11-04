from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint="**",
    
    api_key="**",
    api_version="gpt-4.1-mini"
)

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "user",
            "content": "Explain Azure Kubernetes Service"
        }
    ]
)

print(response.choices[0].message.content)
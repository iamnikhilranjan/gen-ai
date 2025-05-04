from dotenv import load_dotenv

from openai import OpenAI


load_dotenv()

client = OpenAI()

text = "Effiel Tower is famus landmark, it is 324m tall"

response = client.embeddings.create(
    imput = text,
    model = "text-embedding-3-small"
)

print("vector Embeddings", response.data[0].embedding)



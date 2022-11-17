import os
import openai
import argparse
from dotenv import load_dotenv

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", type=str, required=True, help="string")
args = parser.parse_args()

try:
    archive = args.file
except Exception as error:
    print(f"Error: {error}")
    exit()

file = open(archive, "r")
text = "Resumir esto: \n\n" + file.read()
file.close()

# text.insert(0, "Resumir esto: \n\n")

print(text)

print("\nEmpezando a resumir....")

# file2 = open("transcription/summary.txt")

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
    model="text-davinci-002",
    prompt=text,
    temperature=0.7,
    max_tokens=64,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
)

print(response)
print("\nResumen completado...")

for i in response["choices"]:
    print(i["text"])
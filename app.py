import whisper
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-a", "--audio", type=str, required=True, help="string")
args = parser.parse_args()

try:
    audio = args.audio
except Exception as error:
    print(f"Error: {error}")
    exit()

model = whisper.load_model("medium")
result = model.transcribe(audio, fp16=False, language="Spanish")

outf = open("transcription/transcriber.txt", "a")
for i in result["segments"]:
    line = i["text"]
    outf.writelines(line + "\n")
outf.close()

print(result["text"])
print("\nTranscripción completada...")
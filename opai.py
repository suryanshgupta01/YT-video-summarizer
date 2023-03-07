import openai as o
# get openai api key fron their website
from youtube_transcript_api import YouTubeTranscriptApi
# install youtubetransscirt api from the command below
# pip install youtube-transcript-api


x = YouTubeTranscriptApi.get_transcript('stM8dgcY1CA')
# x = YouTubeTranscriptApi.get_transcript('{youtube video code}')
s = "summarize this in 200 words :\n"
for i in range(len(x)):
    if (len(s) > 2024):
        break
    s += x[i]["text"]

o.api_key = "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"
# o.api_key = "{openai api}"

model_engine = "text-davinci-003"
# enter custom prompt to get answer like chatgpt
# prompt = str(input())
prompt2 = "summarize the book 48 laws of power"
completion = o.Completion.create(
    engine=model_engine,
    prompt=s,
    max_tokens=2024, n=1, stop=None, temperature=0.5
)
response = completion.choices[0].text

print(response)

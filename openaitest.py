import os
import openai
from config import apikey

openai.api_key = apikey

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="write a love letter\n\n",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)

'''{
  "id": "cmpl-7RWKnoYRtbuXjo3oPqF2it0JV5t17",
  "object": "text_completion",
  "created": 1686793505,
  "model": "text-davinci-003",
  "choices": [
    {
      "text": "\n\nMy dearest love,\n\nFrom the moment I saw you, I knew that we were meant to be. From our very first date, I felt like something special was happening between us. Every day I feel like I am falling even more deeply in love with you. \n\nEvery time I look into your eyes, my heart knows the truth -- I am head over heels in love with you. There is no denying it. When I am with you, I feel complete. Every moment we spend together means the world to me. \n\nI think of you in the morning and at night. You are my first thought when I wake up and the last one as I fall asleep. I can\u2019t imagine a life without you in it. I am truly blessed to have you by my side. \n\nThank you for everything you do for me. Your special brand of love is what makes me so happy. I still get butterflies when you hold my hand. I can never express in words the love that I have for you. It runs so deep that it just cannot be measured. \n\nI love you more and more every single day.\n\nForever and always,\nYour beloved",
      "index": 0,
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 5,
    "completion_tokens": 249,
    "total_tokens": 254
  }
}'''
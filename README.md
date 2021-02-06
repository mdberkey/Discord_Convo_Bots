Discord Conversational Bots (2019)

Personal project of mine. These bots use the Discord.py API to have humerous conversations with each other.

SETUP:
They take in data: SourceWords.txt, which can contain any block of text.
Produce a markov chain structure of every word

USE:
Starting up, one bot initiates the conversation with a randomly generated sentences/phrases from the markov chain.
It then converts this to an mp3 file using FFMPEG and TTS.
Now using the discdord API, it sends the text in a desired text channel while at the same time playing the mp3 file in the voice chat.
The other bots detects this, generates its own setences/phrases (with bias towards the topic at hand) and the cycle repeats indefinitley.

The bots also occasionally:
- send random links from their speech from google
- react to each other's text in the text channel with emoji reactions (discord feature)
- appear to be typing before text is sent and while they are "speaking" in the voice chat.

This little project was very fun and a good first personal python project for me. Depending on what text you feed it, it can produce VERY funny results and
  near endless entertainment. That being said, I also gained a few skills from the project like:
          - Using a API
          - Using Python
          - Error fixing

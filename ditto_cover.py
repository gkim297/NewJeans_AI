from gtts import gTTS
import os
from pydub import AudioSegment
from pydub import AudioSegment
from pydub.playback import play


song_lyrics = """
Woo woo woo woo ooh
Woo woo woo woo
Stay in the middle
Like you a little
Don't want no riddle
말해줘 say it back
Oh say it ditto
아침은 너무 멀어
So say it ditto

훌쩍 커버렸어
함께한 기억처럼
널 보는 내 마음은
어느새 여름 지나 가을
기다렸지 all this time
Do you want somebody
Like I want somebody
날 보고 웃었지만
Do you think about me now yeah
All the time yeah
All the time

I got no time to lose
내 길었던 하루
난 보고 싶어
Ra-ta-ta-ta 울린 심장 (Ra-ta-ta-ta)
I got nothing to lose
널 좋아한다고 wooah wooah wooah
Ra-ta-ta-ta 울린 심장 (Ra-ta-ta-ta)
But I don't want to

Stay in the middle
Like you a little
Don't want no riddle
말해줘 say it back
Oh say it ditto
아침은 너무 멀어
So say it ditto
I don't want to
Walk in this 미로
다 아는 건 아니어도
바라던 대로
말해줘 Say it back
Oh say it ditto
I want you so, want you
So say it ditto

Not just anybody
너를 상상했지
항상 닿아있던
처음 느낌 그대로 난
기다렸지 all this time

I got nothing to lose
널 좋아한다고 wooah wooah wooah
Ra-ta-ta-ta 울린 심장 (Ra-ta-ta-ta)
But I don't want to

Stay in the middle
Like you a little
Don't want no riddle
말해줘 say it back
Oh say it ditto
아침은 너무 멀어
So say it ditto
I don't want to
Walk in this 미로
다 아는 건 아니어도
바라던 대로
말해줘 Say it back
Oh say it ditto
I want you so, want you
So say it ditto

Woo woo woo woo ooh
Woo woo woo woo"""

# Step 2: Generate AI vocals using gTTS
tts = gTTS(text=song_lyrics, lang='en')  # You can set the language here
tts.save('ai_vocals.mp3')


instrumental_path = 'ditto_inst.mp3'
AudioSegment.converter = "path_to_ffmpeg_executable"  # Replace with the actual path


ai_vocals = AudioSegment.from_mp3('from.mp3')
instrumental = AudioSegment.from_mp3(instrumental_path)

mixed_audio = instrumental.overlay(ai_vocals, position=0)

mixed_audio.export('ai_cover_song.mp3', format='mp3')

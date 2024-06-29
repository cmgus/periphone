from pydub import AudioSegment

song = AudioSegment.from_file("./audios/night-dancer.wav", format="wav")
background_song = AudioSegment.from_file("./background-reggaeton-1-hour.wav")
background_song_duration = background_song.duration_seconds

gap = 10 * 1000

start_time = gap
end_time = start_time + gap
first_10_second = background_song[:start_time]
first_10_second.export("./dist/first_10_second.wav", format="wav")
# start_time = 10000
# end_time = 20000

# segment = song[start_time:end_time]

# segment -= 10

# song = song[:start_time] + segment + song[end_time:]

# song.export("./audios/test.wav", format="wav")

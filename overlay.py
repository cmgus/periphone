from pydub import AudioSegment

salud_visual_audio = AudioSegment.from_file("./audios/audio-salud-visual.wav", format="wav")
# ecocine_audio = AudioSegment.from_file("./audios/audio-ecocine.wav", format="wav")
# background = AudioSegment.from_file("./night-dancer.wav", format="wav")
background1 = AudioSegment.from_file("./audios/audio-villancicos-djanthony.mp3", format="mp3")
gap = AudioSegment.silent(30 * 1000)
mix = salud_visual_audio.append(gap, crossfade=0)
# mix = salud_visual_audio.append(ecocine_audio, crossfade=0)

periphone_audio1 = background1.overlay(mix, position=10000, gain_during_overlay=-7, loop=True)
# periphone_audio = background.overlay(salud_visual_audio, position=10000, gain_during_overlay=-7, loop=True)
# song1 = AudioSegment.from_file("./audios/audio-salud-visual.wav", format="wav")
# song2 = AudioSegment.from_file("./night-dancer.wav", format="wav")

background2 = AudioSegment.from_file("./audios/audio-villancicos-djjarigo.mp3", format="mp3")
periphone_audio2 = background2.overlay(mix, position=10000, gain_during_overlay=-7, loop=True)


periphone_audio = periphone_audio1 + periphone_audio2

periphone_audio.export("./dist/periphone-gain.mp3", format="mp3")
# result = song2.overlay(song1, position=10000, gain_during_overlay=-8, loop=True)


# result.export("./dist/result.wav", format="wav")
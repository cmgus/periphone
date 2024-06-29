from gtts import gTTS

text = """
¡Vecino, vecina de chen chen!
Llega Ecocine, ¡Tarde de Pelis!. Donde se proyectará, "La era del hielo: Las aventuras de Scrat".
Ven con tus botellas de plástico:
Con 3 botellas canjea tú entrada.
Con 7 botellas obtén una entrada más una canchita.
Con 10 botellas gana una entrada más una canchita más una bebida.
Con 15 botellas tendrás 2 entradas más 1 canchita y 2 bebidas.

Ven y participa, este viernes 8 de diciembre en el auditoria de la municipalidad del centro poblado de chen chen, a partir de las 5 y 30 de la tarde. Los esperamos.
"""
tts = gTTS(text, lang="es", tld="com.mx", slow=False)

tts.save("./audios/test-speech.wav")
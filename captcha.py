import random
from captcha.audio import Audiocaptcha 

def generate_random_captcha(lenght=6):
    characters = '1234567890'
    captcha_text = ''.join(random.choices(characters, k=lenght))
    return captcha_text 

audio = Audiocaptcha()
captcha_text = generate_random_captcha()
print("Generate CAPTCHA text, captcha_text")
audio_captcha = audio.generate(captcha_text)
audio.write(captcha_text, 'Audio_captcha.wav')
print("Audio CAPTCHA generate: Audio_captcha.wav")
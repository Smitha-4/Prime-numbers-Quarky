import time
from quarky import *
from speech_recognition import SpeechRecognition
from text_to_speech import TextToSpeech

# Initialize the Robot's Senses
sr = SpeechRecognition()
tts = TextToSpeech()

def check_prime_logic(n):
    if n < 2:
        return False, None
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False, i  # Found a factor!
    return True, None

while True:
    # 1. Start the mission
    quarky.set_led_color(all, [0, 0, 255]) # Blue: Waiting for command
    tts.speak("Arjun, I'm ready for the Math Emergency! Give me a number.")
    
    # 2. Listening for the kid's voice
    sr.listen(timeout=5)
    voice_input = sr.recognized_text()
    
    if voice_input:
        try:
            num = int(voice_input)
            is_prime, factor = check_prime_logic(num)
            
            # 3. Presenting the Results
            if is_prime:
                # Prime Case
                quarky.set_led_color(all, [0, 255, 0]) # Green: Success!
                tts.speak(f"Success! {num} is a Prime Number. It is a VIP and has no factors except one and itself!")
            else:
                # Composite Case
                quarky.set_led_color(all, [255, 0, 0]) # Red: Not Prime
                if num < 2:
                    tts.speak(f"{num} is not prime. Prime numbers must be 2 or greater.")
                else:
                    tts.speak(f"Oh no! {num} is a composite number because it can be divided by {factor}.")
                    
        except ValueError:
            tts.speak("I only understand numbers right now. Try saying a number like 7 or 10!")
    
    time.sleep(2)


# Lets use an inside voice!!

def indoor_str(voice):
    quiet_voice = voice.lower()
    return quiet_voice

outdoor_voice = str(input("Say something loud.."))
print(indoor_str(outdoor_voice))


def playback():
    speech = str(input("say summin"))
    slow = speech.replace(" ", "...")
    return slow

print(playback())

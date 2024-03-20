
def convert(smiley):
    emoji = smiley.replace(":)", "🙂")
    emoji = emoji.replace(":(", "🙁")
    return emoji

def main():
    text_face = str(input("say summin.. "))
    replace_emoji = convert(text_face)
    return replace_emoji

print(main())

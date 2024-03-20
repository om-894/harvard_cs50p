
import emoji

def main():
    emoj = str(input("").lower())

    if ':earth_asia:' in emoj:
        new_moji = emoji.emojize(emoj, language='alias')
        print(new_moji)

    elif '_' in emoj:
        new_moji = emoji.emojize(emoj)
        print(new_moji)

    else:
        new_moji = emoji.emojize(emoj, language='alias')
        print(new_moji)

main()

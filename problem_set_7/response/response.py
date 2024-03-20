
from validator_collection import checkers

def main():
    print(validate(input("whats your email address? ")))

def validate(email):
    valid = checkers.is_email(email)
    if valid:
        return "Valid"
    else:
        return "invalid"





if __name__ == "__main__":
    main()

def solution(phone_number):
    new=(len(phone_number)-4)*"*"+phone_number[-4:]
    return new
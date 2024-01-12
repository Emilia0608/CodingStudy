def solution(phone_book):
    phone_book.sort()
    answer = True
    for index, phone in enumerate(phone_book[:-1]):
        if phone_book[index+1].startswith(phone):
            answer=False
            break
    return answer
    
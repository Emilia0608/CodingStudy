def solution(babbling):
    speak_words=["aya", "ye", "woo", "ma"]
    answer=0
    for bab in babbling:
        word_len=0
        for word in speak_words:
            if word in bab:
                word_len=word_len+len(word)
        if word_len==len(bab):
            answer+=1
    return answer
        
        
        
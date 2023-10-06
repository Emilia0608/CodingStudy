def solution(my_string, overwrite_string, s):
    o_num=len(overwrite_string)
    answer = my_string[:s]+overwrite_string+my_string[s+o_num:]
    return answer


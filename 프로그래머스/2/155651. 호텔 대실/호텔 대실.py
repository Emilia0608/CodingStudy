def solution(book_time):
    book_time.sort(key= lambda x:x[0])
    room_booked={}
    room_count=0
    for i, book in enumerate(book_time):
        check_in_hour=int(book[0].split(':')[0])
        check_in_minute=int(book[0].split(':')[1])
        check_in=check_in_hour*60+check_in_minute

        check_out_hour=int(book[1].split(':')[0])
        check_out_minute=int(book[1].split(':')[1])
        check_out=check_out_hour*60+check_out_minute
        if i==0:
            room_count+=1
            room_booked[room_count]=check_out
        else:
            if check_in-min(list(room_booked.values()))>=10:
                reversed = dict((v,k) for k,v in room_booked.items())
                change_num=reversed[min(list(room_booked.values()))]
                room_booked[change_num]=check_out
            else:
                room_count+=1
                room_booked[room_count]=check_out
    answer = len(room_booked)
    return answer
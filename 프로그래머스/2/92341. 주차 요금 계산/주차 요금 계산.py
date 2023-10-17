import math
def solution(fees, records):
    car_in={}
    car_jucha_sum={}
    car_fee={}
    
    for record in records:
        now_time=int(record.split(' ')[0].split(':')[0])*60+int(record.split(' ')[0].split(':')[1]) #현재 시간
        if record.split(' ')[1] not in list(car_in.keys()): #없는 경우 무조건 in
            car_in[record.split(' ')[1]]=now_time        
            if record.split(' ')[1] not in list(car_jucha_sum.keys()):
                car_jucha_sum[record.split(' ')[1]]=0 #계정 파기
        elif record.split(' ')[2]=="IN":#출차 기록이 없을 때
            out_time=23*60+59
            in_time=car_in.get((record.split(' ')[1]))
            jucha_time=out_time-in_time
            car_jucha_sum[record.split(' ')[1]]=car_jucha_sum[record.split(' ')[1]]+jucha_time

            car_in[record.split(' ')[1]]=now_time #현 기록으로 시간 교체

        else: #입차 기록이 있고 출차기록이 나올 때
            in_time=car_in.get((record.split(' ')[1]))
            jucha_time=now_time-in_time
            car_jucha_sum[record.split(' ')[1]]=car_jucha_sum[record.split(' ')[1]]+jucha_time
            del car_in[record.split(' ')[1]]
            
    # 마지막 기록이 출차가 아닐 때        
    car_num=list(car_jucha_sum.keys())
    for car in car_num:
        if car_in.get(car)!=None: 
            out_time=23*60+59
            jucha_time=out_time-car_in.get(car)
            car_jucha_sum[car]=car_jucha_sum[car]+jucha_time
    
    # 요금 계산
    for car in car_num:
        if car_jucha_sum[car]<=fees[0]:
            total_fee=fees[1]
        else:
            total_fee=fees[1]+math.ceil((car_jucha_sum[car]-fees[0])/fees[2])*fees[3]
        car_fee[car]=total_fee
    answer=[]
    for cf in sorted(car_fee.items()):
        answer.append(cf[1])
    
    return answer



        
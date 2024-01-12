from datetime import datetime, timedelta
def solution(today, terms, privacies):
    term_dict={}
    today=datetime.strptime(today, '%Y.%m.%d')
    today=today+timedelta(days=1)
    if today.day>29:
        today=today-timedelta(days=28)
        today=today+timedelta(months=1)
    print(today.day)
    for term in terms:
        term_dict[term.split(' ')[0]]=int(term.split(' ')[1])
    answer=[]
    for i, privacy in enumerate(privacies):
        yuji_gigan=term_dict[privacy.split(' ')[1]]
        dd=int(privacy.split(' ')[0].split('.')[2])
        mm=int(privacy.split(' ')[0].split('.')[1])
        yy=int(privacy.split(' ')[0].split('.')[0])
        yy=(mm+yuji_gigan)//12+yy
        mm=(mm+yuji_gigan)%12
        if mm==0:
            mm=12
            yy-=1
        mangi_date=datetime(yy,mm,dd)
        print(i+1, mangi_date, today)
        if today>mangi_date:
            answer.append(i+1)
    return answer


# today="2020.01.01"
# terms=["Z 3", "D 5"]
# privacies=["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
# term_dict={}
# today=datetime.strptime(today, '%Y.%m.%d')
# today=today+timedelta(days=1)
# if today.day>29:
#     today=today-timedelta(days=28)
#     today=today+timedelta(months=1)
# print(today.day)
# for term in terms:
#     term_dict[term.split(' ')[0]]=int(term.split(' ')[1])
# answer=[]
# for i, privacy in enumerate(privacies):
#     yuji_gigan=term_dict[privacy.split(' ')[1]]
#     dd=int(privacy.split(' ')[0].split('.')[2])
#     mm=int(privacy.split(' ')[0].split('.')[1])
#     yy=int(privacy.split(' ')[0].split('.')[0])
#     yy=(mm+yuji_gigan)//12+yy
#     mm=(mm+yuji_gigan)%12
#     if mm==0:
#         mm=12
#         yy-=1
#     mangi_date=datetime(yy,mm,dd)
#     print(i+1, mangi_date, today)
#     if today>mangi_date:
#         answer.append(i+1)
# print(answer)
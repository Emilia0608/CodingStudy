import itertools
from collections import Counter
def solution(orders, course):
    course_dict={}
    for c in course:
        combination_list=[]
        for order in orders:
            nPr = itertools.combinations(order, c)
            for np in list(nPr):
                combination=''
                np=sorted(np) # 각 조합 알파벳순 정렬 필요, XY=YX가 되기 위해
                for i in range(0, len(np)):
                    combination+=np[i]
                if combination!=[]:
                    combination_list.append(combination)
        if len(combination_list)!=0: # 조합이 될 경우만 count
            course_dict[c]=Counter(combination_list)
    answer=[]
    for c in list(course_dict.keys()):
        c_max_value=course_dict[c].most_common()[0][1]
        if c_max_value==1: # 1명만 조합한게 최대일경우는 제외
            pass
        else:
            popular_course=[]
            for common in course_dict[c].most_common():
                if common[1]!=c_max_value:
                    break
                else:
                    popular_course.append(common[0])
            answer.extend(popular_course)
    answer.sort() # 오름차순 정렬
    return answer


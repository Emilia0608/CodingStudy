def solution(genres, plays):
    genres_dict={}
    for i in range(len(genres)):
        if genres[i] not in genres_dict:
            genres_dict[genres[i]]={}
            genres_dict[genres[i]]["play_cnt"]=0
            genres_dict[genres[i]]["most_play"]=[]

        genres_dict[genres[i]]["play_cnt"]+=plays[i]

        if len(genres_dict[genres[i]]["most_play"])<2: # 아직 장르별 노래가 2개 미만일 때
            genres_dict[genres[i]]["most_play"].append([i, plays[i]])
            genres_dict[genres[i]]["most_play"]=sorted(genres_dict[genres[i]]["most_play"], key=lambda x:x[1], reverse=True)
        else:
            genres_dict[genres[i]]["most_play"]=sorted(genres_dict[genres[i]]["most_play"], key=lambda x:x[1], reverse=True)
            if genres_dict[genres[i]]["most_play"][-1][1]<plays[i]: # 현재 노래가 장르별 노래 top2 보다 더 많은 재생 수 일 때
                genres_dict[genres[i]]["most_play"].pop()
                genres_dict[genres[i]]["most_play"].append([i, plays[i]])
                genres_dict[genres[i]]["most_play"]=sorted(genres_dict[genres[i]]["most_play"], key=lambda x:x[1], reverse=True)
    genres_dict = sorted(genres_dict.items(), key=lambda x: x[1]["play_cnt"], reverse=True)
    answer=[]
    for key, value in genres_dict:
        answer.extend([play[0] for play in value["most_play"]])
    return answer
# import requests
# import showGoldenKey
#
# url = {"init" : "http://15.165.88.215:8888/init",                                   # 초기화
#        "playerInfo" : "http://15.165.88.215:8888/player/{}",
#        "getGoldenKey" : "http://15.165.88.215:8888/key/{}",                         # 황금열쇠 받기
#        "move" : "http://15.165.88.215:8888/player/move?user_id={}&dice_value={}",   # 움직임
#        "bankruptcy" : "http://15.165.88.215:8888/player/bankruptcy/{}",             # 파산
#        "pay" : "http://15.165.88.215:8888/player/toll?userID={}&cityID={}&usingShield={}",  # 통행료 지불
#        "payInfo" : "http://15.165.88.215:8888/player/toll?cityID={}",                       # 통행료 정보
#        "getLand" : "http://15.165.88.215:8888/area/{}",                                     # 땅 정보 가져오기
#        "Landcost" : "http://15.165.88.215:8888/area/buy/{}/cost?villa=1&building=0&hotel=0", # 구입 금액
#        "buyLand" : "http://15.165.88.215:8888/area/buy/{}?userID={}&villa=1&building=0&hotel=0",    # 땅 구입
#        "upgradeLand" : "http://15.165.88.215:8888/area/upgrade/{}?user_id={}&villa={}&building={}&hotel={}", # 땅 업그레이드
#        "upgradecost" : "http://15.165.88.215:8888/area/upgrade/{}/cost?villa={}&building={}&hotel={}",      # 땅 업그레이드 금액
#        "funding" : 'http://15.165.88.215:8888/area/social/reception?user_id={}',    # 사회 복지기금 내기
#        "fund" : "http://15.165.88.215:8888/area/social/dispatch?user_id={}"         # 사회 복지기금 받기
#         }
#
# print(requests.get(url["getLand"].format(30)).json())


l = [1,0]
x,y = l
print(x,y)
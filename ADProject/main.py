import pickle
import sys

city = ['강남구', '강동구', '강북구', '노원구', '도봉구', '동대문구']

try:
    f = open('user data.txt', 'rb')
    data = pickle.load(f)
    print(data)
    f.close()
except:
    f = open('user data.txt', 'wb')
    data = []
    data.append(input("성별을 입력해주세요: "))
    data.append(input("나이를 입력해주세요: "))
    data.append(input("현재 거주중인 지역을 입력해주세요: "))
    while data[2] not in city:
        data[2] = input("존재하지 않는 지역입니다. 다시 한번 거주중인 지역을 입력해주세요: ")
    pickle.dump(data, f)
    f.close()
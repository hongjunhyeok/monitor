#! /user/bin/py

import time



def temperatuere(value, displacement=None):
    if not displacement:
        displacement= (0,1,1,2,-1,-1,-2,0,-1,-1,-2,2,2,0)
    current = 0


    while True:
        value += displacement[current]
        current = (current +1)%len(displacement)
        yield value

from threading import Thread


## on_change 값이 변하면 처리할때쓰임 콜백함수는 on 으로 시작한다.
## interval 간격 1초
## 전략패턴 사용 뭘 호출할것인지만 신경쓴다.
class TemperatureSensor(Thread):
    def __init__(self, value = 0,displacement=None, interval=1, on_change=None):
        Thread.__init__(self)
        self.sensor=temperatuere(value, displacement)## 제네레이터 객체가 리턴된다.
        self.value = value
        self.interval = interval
        self.on_change = on_change


    def measure(self):
        return self.value


    # def run(self): #interval 간격으로 센서 값 갱신
    #     while True:
    #         time.sleep(self.interval)
    #         ## 제네레이터 확인
    #         value = self.sensor.__next__()
    #
    #         ## 이벤트 정의 내리고 핸들러 작동시킴
    #         if self.on_change:
    #             self.on_change(value)


    def run(self):
        try:
            for self.value in self.sensor:
                time.sleep(self.interval)
                if self.on_change:
                    self.on_change(self.value)
        except:
            print('센서 스레드가 종료합니다.')

if __name__=='__main__':
    #print(temperatuere)


    # t =제네레이터 인스턴스
    # t = temperatuere(10)
    # print(t)



    # t = temperatuere(10)
    # print(t)
    # print(t.__next__())
    # print(t.__next__())


    # for value in temperatuere(5):
    #     print(value)
    #     time.sleep(1)
    #test  코드


    ts =TemperatureSensor(on_change=lambda  v:print(v))
    ts.start()
    print('선서 기동')
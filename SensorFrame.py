import sys
from tkinter import *
from tkinter.ttk import *
from temperature import TemperatureSensor
class SensorFrame(Frame):
    def __init__(self,master,category = '',location = '',value =0):
        Frame.__init__(self,master) # 마스터는 부모 윈도우 # 다중상속을 대비해 super로 상속하지 않는다.

        self.master = master
        self.master.title('sensor : '+ category)
        self.pack(fill=BOTH,expand=True)#부모윈도우에 맞게 조정

        self.scale = Scale(self, from_=0 ,to = 100 , orient=VERTICAL )
        self.scale.pack(ipadx=10,ipady=0,side=LEFT)#크기조정 불가

        self.lb1Value = Label(self)
        self.lb1Value.pack(side =LEFT, fill = X , padx =10, expand = True)# 높이고정 x축 늘림가능

        self.sensor = TemperatureSensor(value, on_change=lambda v:self.on_change(v))
        self.sensor.start()
        self.set_value(self.sensor.measure())

        ## 사용하는 측에서
        ## 딴데서 쓸려고 분리했다.
        ## 스크롤 할때 위치조정하기위해 생겨난 메서드
    def set_value(self,value):
        self.lb1Value.config(text ='온도 : '+ str(value))
        # print(value, 50-value)
        self.scale.set(50-value)


        ## 딴데서 쓸려고 분리했다.
    def on_change(self,value):
        self.set_value(value)



#   초기값을 미리 정하는경우
# def main():
#     value = 10
#     if len(sys.argv) > 1 :
#         value = int(sys.argv[1])
#
#     root = Tk()
#     root.geometry("200x100+100+100")
#     # SensorFrame(root, 'temperature','livingroom',value)
#     SensorFrame(root,'temperature','livingroom',value)
#     root.mainloop()


# 매개변수로 바꾸는 방법
def main():
    value = 10
    category = 'temperature'
    location = 'living room'
    if len(sys.argv) > 1 :
        category = sys.argv[1]
        location = sys.argv[2]
        value = int(sys.argv[3])

    root = Tk()
    root.geometry("200x100+100+100")
    # SensorFrame(root, 'temperature','livingroom',value)
    SensorFrame(root,category,location,value)
    root.mainloop()


if __name__ == '__main__':
    main()
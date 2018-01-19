import sys
from tkinter import *
from actor.light import Light
import paho.mqtt.client as mqtt
from datetime import datetime
from actor.light import Light
from threading import Thread


## Frame 상속받음
class  LightFrame(Frame):
    def __init__(self,master,category='',location='',value=0):
        Frame.__init__(self,master,bg='black')## 프레임 생성시 블랙줌.
        self.client = mqtt.Client()  # client 오브젝트 생성
        self.master=master
        self.master.title('전등 : ' +category)
        self.pack(fill=BOTH, expand =True)


        self.light = Light(self)
        self.light.pack(side = LEFT, expand =True)

        self.topic=''

        self.lightButton = Button(self, text ='전등button',
                                  command=lambda :self.on_light_btn_click(self.client,self.topic))
        self.lightButton.pack(side=LEFT, expand= True)
        self.status=False


    def on_light_btn_click(self,client,topic):
        self.light.status= not self.light.status
        topic ='ygyg331'

        if self.light.status:
            self.turn_on()
           # client.publish("ygyg331", 'ON' + '*' + str(datetime.now())[0:19])
            client.publish("ygyg331","led")
            print(topic)


        else:
            self.turn_off()
           # client.publish("ygyg331", 'OFF' + '*' + str(datetime.now())[0:19])
            client.publish("ygyg331","led-off")

            print(topic)

        client.loop(2)




    def turn_on(self):

        self.light.turn_on()
        self.lightButton.config(text='전등 끄기')
        self.light.config(bg='white')
        Frame.config(self,bg='white')
       # client.publish(topic, 'ON' + '///' + str(datetime.now())[0:19])


    def turn_off(self):

        self.light.config(bg='black')
        Frame.config(self,bg='pink')
        #client.publish(topic,'OFF'+'***'+str(datetime.now()))

        #이벤트 핸들러 끝.





def main():
    root =Tk()
    root.geometry("300x100+100+100")
    location = 'livingroom'
    light=Light(root)
    client=mqtt.Client()
    client.connect('localhost',1883)
    client.loop(1)
    topic='ygyg331'
    # if len(sys.argv) >1 :
    # 
    #     location = sys.argv[1]


    app = LightFrame(root,location)
    root.mainloop()
    try:
        Thread()
    except Exception as err:
        print('err : %s' % err)


if __name__ == '__main__':
    main()


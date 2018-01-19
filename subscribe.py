import paho.mqtt.client as mqtt
import time

# call back function that have results about connection trying to broker
light_status = ['///','///']
def on_connect(client, userdata, flags, rc):
    print("connected with result code " + str(rc))


    client.subscribe("ygyg331") # ygyg331 구독




# def on_message(client, userdata, msg):
#     value=msg.payload.decode('utf-8')
#     topics = msg.topic.split('/')
#     device_group=topics[2]
#
#     device = topics[3]
#     if device == 'light1':
#         light_status[0]=value
#     elif device =='light2':
#         light_status[1]=value
#     print('------------------------------------------')
#     print('[%s]'%device_group)
#     print('light1:%s'%light_status[0])
#     print('light2:%s'%light_status[1])
#     print('------------------------------------------')




# def on_message(client, userdata, msg):
#     value = msg.payload.decode('utf-8')
#
#     topics = msg.topic.split('/')
#     device_group=topics[2]
#     print('group=%s'%device_group)
#
#     device = topics[3]
#     print('device = %s'%device)
# #when we don't know what they come
#     if not device_group in device_status.keys():
#         device_status[device_group]={}
#
#     device_status[device_group][device] =value
#device_status={}
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload)) #토픽과 메세지를 출력한다.






    

    
        


try:
    client = mqtt.Client()  # client 오브젝트 생성


    client.on_connect = on_connect  # 콜백설정
    client.on_message = on_message  # 콜백설정
    client.connect('localhost', 1883, 60)

    client.loop_forever()
except Exception as err:
    print( 'err : %s'%err)

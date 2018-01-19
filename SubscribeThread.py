import paho.mqtt.client as mqtt
from threading import Thread

class SubscribeThread(Thread):
    def __init__(self, handler):
        super().__init__()

        # 1. MQTT 클라이언트 객체 인스턴스화
        self.client = mqtt.Client()

        # 2. 관련 이벤트에 대한 콜백 함수 등록
        self.client.on_connect = lambda *args : self.on_connect(*args)
        self.client.on_message = lambda *args : self.on_message(*args)
        self.handler = handler
    # 브로커 접속 시도 결과 처리 콜백 함수
    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print('연결 성공')
            self.client.subscribe("home/iot/#")  # 연결 성공시 토픽 구독 신청
        else:
            print('연결 실패 :  ', rc)

    # 관련 토픽 메시지 수신 콜백 함수
    def on_message(self, client, userdata, msg):
        self.handler(msg)

    def run(self):
        try:
            # 3. 브로커 연결
            self.client.connect("localhost")
            # 4. 메시지 루프 - 이벤트 발생시 해당 콜백 함수 호출됨
            self.client.loop_forever()
        except Exception as err:
            print('에러 : %s' % err)

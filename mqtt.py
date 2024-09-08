import time
from umqtt.simple import MQTTClient

class MQTTClientManager:
    def __init__(self, client_id, server, port=1883, username=None, password=None, keepalive=60):
        self.client_id = client_id
        self.server = server
        self.port = port
        self.username = username
        self.password = password
        self.keepalive = keepalive
        self.client = None

    def connect(self):
        """连接到 MQTT 服务器"""
        self.client = MQTTClient(self.client_id, self.server, port=self.port,
                                 user=self.username, password=self.password, keepalive=self.keepalive)
        try:
            self.client.connect()
            print("MQTT 连接成功")
        except Exception as e:
            print("MQTT 连接失败:", e)

    def disconnect(self):
        """断开与 MQTT 服务器的连接"""
        if self.client:
            self.client.disconnect()
            print("MQTT 连接已断开")
    
    def subscribe(self, topic):
        """订阅指定的主题"""
        if self.client:
            try:
                self.client.subscribe(topic)
                print(f"已订阅主题: {topic}")
            except Exception as e:
                print(f"订阅主题失败: {e}")
    
    def publish(self, topic, msg):
        """向指定主题发布消息"""
        if self.client:
            try:
                self.client.publish(topic, msg)
                print(f"已发布消息到主题 {topic}: {msg}")
            except Exception as e:
                print(f"发布消息失败: {e}")
    
    def set_callback(self, callback):
        """设置回调函数，用于接收消息"""
        if self.client:
            self.client.set_callback(callback)
    
    def check_messages(self):
        """检查是否有新的消息"""
        if self.client:
            try:
                self.client.check_msg()  # 非阻塞地检查消息
            except Exception as e:
                print(f"消息检查失败: {e}")

    def wait_for_message(self):
        """阻塞等待接收到新的消息"""
        if self.client:
            try:
                self.client.wait_msg()  # 阻塞等待消息
            except Exception as e:
                print(f"等待消息失败: {e}")

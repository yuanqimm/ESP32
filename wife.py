import network
import time
from machine import Pin

class WiFiManager:
    def __init__(self, ssid, password, pin=None):
        self.ssid = ssid
        self.password = password
        self.pin = pin
        self.wlan = network.WLAN(network.STA_IF)
        self.led = Pin(pin, Pin.OUT) if pin is not None else None
        self.wlan.active(True)

    def connect(self, timeout=20):#连接WiFi
        if not self.wlan.isconnected():
            print("正在连接网络...")
            self.wlan.connect(self.ssid, self.password)
            start_time = time.time()

            while not self.wlan.isconnected():
                self._blink_led()
                if time.time() - start_time > timeout:
                    print("Wi-Fi 连接超时！")
                    return False

            print("Wi-Fi 连接成功！")
            self._turn_off_led()
            self.print_info()
            return True
        else:
            print("Wi-Fi 已经连接。")
            self._turn_off_led()
            self.print_info()
            return True

    def disconnect(self):#断开连接
        if self.wlan.isconnected():
            self.wlan.disconnect()
            print("Wi-Fi 已断开连接。")
        else:
            print("Wi-Fi 尚未连接。")

    def _blink_led(self):#LED闪烁
        if self.led is not None:
            self.led.value(1)
            time.sleep_ms(100)
            self.led.value(0)
            time.sleep_ms(100)

    def _turn_off_led(self):
        if self.led is not None:
            self.led.value(0)

    def print_info(self):#WiFi信息
        if self.wlan.isconnected():
            print("IP: {} | 子网掩码: {} | 网关: {} | DNS: {}".format(
                self.wlan.ifconfig()[0], self.wlan.ifconfig()[1], self.wlan.ifconfig()[2], self.wlan.ifconfig()[3]))
        else:
            print("Wi-Fi 尚未连接，无法获取网络信息。")

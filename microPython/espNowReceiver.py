import network
import espnow
import ubinascii


sta = network.WLAN(network.WLAN.IF_STA)
sta.active(True)
sta.disconnect()   # Because ESP8266 auto-connects to last Access Point
sta.config(channel=11)

wlan_mac = sta.config('mac')
print("MAC Address:", wlan_mac)
print(ubinascii.hexlify(wlan_mac, ':').decode().upper())

e = espnow.ESPNow()
e.active(True)

while True:
    host, msg = e.recv()
    if msg:             # msg == None if timeout in recv()
        print(host, msg)
        if msg == b'end':
            break

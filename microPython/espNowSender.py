import network
import espnow
from time import sleep
import ubinascii


# A WLAN interface must be active to send()/recv()
sta = network.WLAN(network.WLAN.IF_STA)  # Or network.WLAN.IF_AP
sta.active(True)
sta.disconnect()   # Because ESP8266 auto-connects to last Access Point
sta.config(channel=11
           )    # Change to the channel used by the proxy above.

wlan_mac = sta.config('mac')
print("MAC Address:", wlan_mac)
print(ubinascii.hexlify(wlan_mac, ':').decode().upper())

e = espnow.ESPNow()
e.active(True)
peer = b'\xff\xff\xff\xff\xff\xff'   # MAC address of peer's wifi interface
e.add_peer(peer)      # Must add_peer() before send()

print('Starting...')
e.send(peer, "Starting...")
for i in range(100):
    e.send(peer, str(i)*20, True)
    print(str(i)*20)
    sleep(1)
e.send(peer, b'end')

# Before using this code
Do not forget to turn on monitor mode and choose the right channel on your wireless interface card.

Here is a exmaple on how to do it : 
```
sudo ifconfig wlp5s0 down
sudo iwconfig wlp5s0 mode monitor
sudo ifconfig wlp5s0 up
sudo iwconfig wlp5s0 channel 1 
```

# Verification

## Before
```
# iwconfig

wlp4s0    IEEE 802.11  ESSID:off/any
          Mode:Managed  Access Point: Not-Associated   Tx-Power=off
          Retry short limit:7   RTS thr:off   Fragment thr:off
          Power Management:on
```

## After
```
# iwconfig

wlp4s0    IEEE 802.11  Mode:Monitor  Frequency:2.412 GHz
          Retry short limit:7   RTS thr:off   Fragment thr:off
          Power Management:on
```

# Possible Issue

## How to resolve:
```
# ifconfig wlp4s0 up
SIOCSIFFLAGS: Operation not possible due to RF-kill

# rfkill list all
2: phy0: Wireless LAN
	Soft blocked: yes
	Hard blocked: no

# rfkill unblock wifi

# rfkill list all
2: phy0: Wireless LAN
	Soft blocked: no
	Hard blocked: no
```


# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
#import webrepl
#webrepl.start()
gc.collect()


from umqtt.simple import MQTTClient
mq = MQTTClient("nomedotopico","broker.emqx.io",1883,"emqx","public")
import network
nic = network.WLAN(network.STA_IF)
nic.active(True)
nic.connect('castroNet', 'castroeribas')
mq.connect()

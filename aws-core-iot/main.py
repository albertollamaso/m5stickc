from m5stack import *
from m5ui import *
from uiflow import *
from IoTcloud.AWS import AWS
import wifiCfg
import json
import hat


# Get speaker
hat_spk_0 = hat.get(hat.SPEAKER)

# Define global variables
wifi_ssid = "SSID"
wifi_password = "wifi_password"
aws_iot_ep_url = "xxxxx-ats.iot.us-east-1.amazonaws.com"
aws_iot_thing_name = "m5stick"
aws_iot_port = 8883
aws_iot_keep_alive = 300
aws_iot_cert = "/flash/res/m5stickc.cert.pem"
aws_iot_key = "/flash/res/m5stickc.private.key"
aws_iot_topic = "mytopic"

alert = None
message = None
description = None
data = None
priority = None

# Connect to WIFI
wifiCfg.doConnect(wifi_ssid, wifi_password)


# Define label fields on screen
label1 = M5TextBox(15, 135, "label1", lcd.FONT_DefaultSmall, 0xFFFFFF, rotate=270)
label2 = M5TextBox(26, 135, "label2", lcd.FONT_DefaultSmall, 0xFFFFFF, rotate=270)
label0 = M5TextBox(0, 135, "label0", lcd.FONT_DefaultSmall, 0xFFFFFF, rotate=270)

# Describe this function...
def parse_alert():
  global alert, message, description, data, priority
  try :
    message = data['message']
    description = data['description']
    priority = data['priority']
    label0.hide()
    label1.hide()
    label2.hide()
    label0.setText(str(message))
    label1.setText(str(description))
    label2.setText(str(priority))
    pass
  except:
    label0.setText(str(data))


def fun_topic_(topic_data):
  global alert, message, description, data, priority
  axp.setLcdBrightness(50)
  label0.setText('checking...')
  wait(1)
  data = json.loads(topic_data)
  parse_alert()
  while alert:
    M5Led.on()
    hat_spk_0.sing(330, 1)
    wait_ms(500)
  wait(2)
  label1.hide()
  label2.hide()
  alert = True
  label0.setText('Listening on ALERTS')
  axp.setLcdBrightness(0)
  M5Led.off()
  pass

def buttonB_wasPressed():
  global alert, message, description, data, priority
  label0.setText('Listening on ALERTS')
  axp.setLcdBrightness(50)
  wait(5)
  axp.setLcdBrightness(0)
  pass
btnB.wasPressed(buttonB_wasPressed)

def buttonA_wasPressed():
  global alert, message, description, data, priority
  alert = False
  M5Led.off()
  pass
btnA.wasPressed(buttonA_wasPressed)


# Start
# Set screen to black
setScreenColor(0x000000)
label0.setText('Starting...')
wait(2)
label0.hide()
label1.hide()
label2.hide()
axp.setLcdBrightness(0)
alert = True
aws = AWS(things_name=aws_iot_thing_name, host=aws_iot_ep_url, port=aws_iot_port, keepalive=aws_iot_keep_alive, cert_file_path=aws_iot_cert, private_key_path=aws_iot_key)
aws.subscribe(aws_iot_topic, fun_topic_)
aws.start()

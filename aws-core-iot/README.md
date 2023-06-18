
# AWS-CORE-IOT

<img src="https://github.com/albertollamaso/m5stickc/blob/main/images/alerting.png" alt="alerting" width="350">


Establish a seamless connection between your device M5stickc and AWS IoT Core and enable data communication via the MQTT protocol.

You can find below the list of variables that you need to modify to accommodate to your setup.


## UI FLOW

<img src="https://github.com/albertollamaso/m5stickc/blob/main/images/uiflow_diagram.jpeg" alt="uiflow" width="350">


```
wifi_ssid = "SSID"
wifi_password = "wifi_password"
aws_iot_ep_url = "xxxxx-ats.iot.us-east-1.amazonaws.com"
aws_iot_thing_name = "m5stick"
aws_iot_port = 8883
aws_iot_keep_alive = 300
aws_iot_cert = "/flash/res/m5stickc.cert.pem"
aws_iot_key = "/flash/res/m5stickc.private.key"
aws_iot_topic = "mytopic"
```


## Sample data

```
{
    "message": "alert message",
    "description": "this is a description",
    "priority": "P3"
}
```

from boltiot import Bolt
import config, Send_alerts
import json, time

api_key = config.api_key
device_id  = config.device_id

mybolt = Bolt(api_key, device_id)

ir_pin = '4'
led_pin = '0'

def get_sensor(pin):
    try:
        data = json.loads(mybolt.digitalRead(pin))
        if data['success'] != 1:
            print('Request Unsuccessful')
            print('Response data ->', data)
            return None
        sensor_value = int(data['value'])
        return sensor_value

    except Exception as e:
        print('An expection occured while returning the sensor value! Details below:')
        print(e)
        return None

prev_value = None
while True:
    sensor_value = get_sensor(ir_pin)
    print(sensor_value)
    
    if sensor_value == 1 and prev_value != 1:
        response = mybolt.digitalWrite(led_pin, 'HIGH')
        Send_alerts.send_mail("Your drawer has been opened", "Someone has opened your drawer. Please ignore this e-mail if it is opened by you. ")
        prev_value = sensor_value

    elif sensor_value == 0 and prev_value != 0:
        response = mybolt.digitalWrite(led_pin, 'LOW')
        prev_value = sensor_value

    time.sleep(10)
    
import requests
from mycroft import MycroftSkill, intent_file_handler



class FrxIot(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        
        
    def send_command(self, unit, command, value):
        cmd = { "id":unit, "command":command, "value":value}
        resp = requests.post('http://10.0.3.100/api/Command', json=cmd)
        if resp.status_code != 201:
            self.speak_dialog('err')
        else: 
            self.speak_dialog('iot.frx')        
        

    @intent_file_handler('light.on.intent')
    def handle_lights_on(self, message):
        self.send_command(self, 'LIGHT-88F3-A567B67D453C', 'white_light_1', '1')
        self.send_command(self, 'LIGHT-88F3-A567B67D453C', 'red_light_1', '1')
        self.send_command(self, 'LIGHT-88F3-A567B67D453C', 'blue_light_1', '1')
        
        
    @intent_file_handler('light.off.intent')
    def handle_lights_off(self, message):
        self.send_command(self, 'LIGHT-88F3-A567B67D453C', 'white_light_1', '0')
        self.send_command(self, 'LIGHT-88F3-A567B67D453C', 'red_light_1', '0')
        self.send_command(self, 'LIGHT-88F3-A567B67D453C', 'blue_light_1', '0')
        
        


def create_skill():
    return FrxIot()


import requests
from mycroft import MycroftSkill, intent_file_handler



class FrxIot(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        
        
    def send_command(self, unit, command, value):
        cmd = { "id":unit, "command":command, "value":value}
        resp = requests.post('http://10.0.3.100/api/Command', json=cmd)
        self.log.info('Requesting Command For Url ....')
        self.log.info(resp.status_code)
        self.log.info(resp.text)
        if resp.status_code != 200:
            self.speak_dialog('err_'+command)
        

    @intent_file_handler('light.on.intent')
    def handle_lights_on(self, message):
        self.send_command('LIGHT-88F3-A567B67D453C', 'white_light_1', '1')
        self.send_command('LIGHT-88F3-A567B67D453C', 'red_light_1', '1')
        self.send_command('LIGHT-88F3-A567B67D453C', 'blue_light_1', '1')
        self.speak_dialog('iot.frx')
        
    @intent_file_handler('light.off.intent')
    def handle_lights_off(self, message):
        self.send_command('LIGHT-88F3-A567B67D453C', 'white_light_1', '0')
        self.send_command('LIGHT-88F3-A567B67D453C', 'red_light_1', '0')
        self.send_command('LIGHT-88F3-A567B67D453C', 'blue_light_1', '0')
        self.speak_dialog('iot.frx')
        
    @intent_file_handler('red_light.intent')
    def handle_lights_red(self, message):   
        self.send_command('LIGHT-88F3-A567B67D453C', 'white_light_1', '0')
        self.send_command('LIGHT-88F3-A567B67D453C', 'red_light_1', '1')
        self.send_command('LIGHT-88F3-A567B67D453C', 'blue_light_1', '0')
        self.speak_dialog('iot.frx')
        
    @intent_file_handler('blue_light.intent')
    def handle_lights_blue(self, message):   
        self.send_command('LIGHT-88F3-A567B67D453C', 'white_light_1', '0')
        self.send_command('LIGHT-88F3-A567B67D453C', 'red_light_1', '0')
        self.send_command('LIGHT-88F3-A567B67D453C', 'blue_light_1', '1')
        self.speak_dialog('iot.frx')
        
    @intent_file_handler('white_lights.intent')
    def handle_lights_white(self, message):   
        self.send_command('LIGHT-88F3-A567B67D453C', 'white_light_1', '1')
        self.send_command('LIGHT-88F3-A567B67D453C', 'red_light_1', '0')
        self.send_command('LIGHT-88F3-A567B67D453C', 'blue_light_1', '0')
        self.speak_dialog('iot.frx')
        
        


def create_skill():
    return FrxIot()


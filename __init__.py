from mycroft import MycroftSkill, intent_file_handler


class FrxIot(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('iot.frx.intent')
    def handle_iot_frx(self, message):
        self.speak_dialog('iot.frx')


def create_skill():
    return FrxIot()


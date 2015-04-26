from talkmoreapi import *
from iegget.settings import TALKMORE_USER, TALKMORE_PASSWD
import os

t = TalkmoreAPI(TALKMORE_USER, TALKMORE_PASSWD)

class SMSTranslator(object):

    @staticmethod
    def send_sms(device, token):
        if device.number[0:2] == '00': number = device.number[4:]
        else: number = device.number[3:]
        t.login()
        t.send_sms([number], "Token: " + token)

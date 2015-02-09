import re

from bender.signals import event_received, message_received


@event_received.connect
def echo(sender, **kwargs):
    print(kwargs['event']._raw)
    return True


@message_received.connect
def hey(sender, **kwargs):
    event = kwargs['event']

    if re.search('hi dave', event.text, re.IGNORECASE):
        sender.slack_client.send_message('Hey.', event.channel)


@message_received.connect
def trolol(sender, **kwargs):
    event = kwargs['event']

    if 'lol' in event.text:
        sender.slack_client.send_message('trololol', event.channel)


@message_received.connect
def marvin(sender, **kwargs):
    event = kwargs['event']

    if re.search("what's wrong", event.text, re.IGNORECASE):
        sender.slack_client.send_message('Everything is wrong.', event.channel)
    if ':simple_smile:' in event.text:
        sender.slack_client.send_message(':disappointed:', event.channel)


@message_received.connect
def always_sure(sender, **kwargs):
    event = kwargs['event']

    if re.search('are you sure', event.text, re.IGNORECASE):
        sender.slack_client.send_message("I'm always sure :sunglasses:", event.channel)

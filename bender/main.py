import os

import slack

from .signals import event_received, message_received


class SlackBot(object):

    def __init__(self):
        pass

    def run(self):
        self.token = os.environ['SLACK_API_TOKEN']
        self.slack_client = slack.SlackRTMClient(self.token)
        self.slack_client.connect()

        while True:
            for event in self.slack_client.read():
                event_received.send(self, event=event)
                if event.type == 'message':
                    message_received.send(self, event=event)


if __name__ == '__main__':
    from .plugins import demo
    bot = SlackBot()
    bot.run()

import blinker

_signals = blinker.Namespace()

event_received = _signals.signal('event-received')
hello_received = _signals.signal('hello-received')
message_received = _signals.signal('message-received')
message_sent = _signals.signal('message-sent')
presence_change = _signals.signal('presence-change')
user_typing = _signals.signal('user-typing')

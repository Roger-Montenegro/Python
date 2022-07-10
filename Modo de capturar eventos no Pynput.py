from pynput import mouse

while True:
    with mouse.Events() as events:
        # Block at most one second
        event = events.get()
        # print(event)
        if type(event) == events.Click and event.pressed:
            print(event.x, events.y, event.button)

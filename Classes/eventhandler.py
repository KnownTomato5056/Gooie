cache = {
    256: set(),
    1024: set(),
    1025: set(),
    1026: set(),
}

eid = {
    'quit': 256,
    'left_button_down': 1025,
    'right_button_down': 1025,
    'left_button_up': 1026,
    'right_button_up': 1026,
    'enter': 1024,
    'leave': 1024,
}

widget_in_focus = None


def collides(pos, widget):
    return widget.rect.collidepoint(pos)


def event_id_translate(event_set: set) -> set:
    translated = set()
    for event in event_set: 
        translated.add(eid[event])
    return translated


def cache_events(widgets: list) -> dict:
    for widget in widgets:
        for eid in event_id_translate(widget.events):
            cache[eid].add(widget)


def handle_mouse_movement_events(event):
    global widget_in_focus
    for widget in cache[1026]:
        if collides(event.dict['pos'], widget):
            if not widget_in_focus:
                widget_in_focus = widget
                if 'enter' in widget.events: widget.on_enter()

            elif widget_in_focus != widget:
                if 'enter' in widget.events: widget.on_enter()
                if 'leave' in widget_in_focus.events: widget_in_focus.on_leave()
                widget_in_focus = widget
            return


    if widget_in_focus:
        if 'leave' in widget_in_focus.events: widget_in_focus.on_leave()
        widget_in_focus = None


def event_pipeline(widget, event):
    if not widget.active: return
    if event.type == 1025:
        if not collides(event.dict['pos'], widget): return
        btn = event.dict['button']
        if btn == 1 and 'left_button_down' in widget.events: widget.on_left_button_down()
        elif btn == 3 and 'right_button_down' in widget.events: widget.on_right_button_down()

    elif event.type == 1026:
        if not collides(event.dict['pos'], widget): return
        btn = event.dict['button']
        if btn == 1 and 'left_button_up' in widget.events: widget.on_left_button_up()
        elif btn == 3 and 'right_button_up' in widget.events: widget.on_right_button_up()


class EventHandler:
    def __init__(self, app):
        self.app = app
        self.widgets = self.app.widgets
        self.cache = cache_events(self.widgets)


    def handle(self, events: list):
        for event in events:
            if event.type == 1024: handle_mouse_movement_events(event)
            elif event.type == 32782: self.app.restore()
            else:
                try:
                    for widget in cache[event.type]: event_pipeline(widget, event)
                except: print(event)

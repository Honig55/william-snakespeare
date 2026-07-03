import datetime

class Debugger():

    active:bool = False
    show_time_stamp:bool = False

    def __init__(self, active:bool=False, show_time_stamp:bool=False):
        self.active = active
        self.show_time_stamp = show_time_stamp

    def dbg(self, message:str):
        if self.active:
            if self.show_time_stamp:
                from datetime import datetime
                print(f"[{datetime.now()}] {message}")
            else:
                print(message)

    def enable(self):
        self.active = True

    def disable(self):
        self.active = False

    def enable_time_stamp(self):
        self.show_time_stamp = True

    def disable_time_stamp(self):
        self.show_time_stamp = False    
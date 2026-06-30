import datetime

class Debugger():

    active:bool = False
    show_time_stamp:bool = False

    __init__(self, active:bool=False, show_time_stamp:bool=False):
        self.active = active
        self.show_time_stamp = show_time_stamp

    dbg(self, message:str):
        if self.active:
            if self.show_time_stamp:
                from datetime import datetime
                print(f"[{datetime.now()}] {message}")
            else:
                print(message)

    enable(self):
        self.active = True

    disable(self):
        self.active = False

    enable_time_stamp(self):
        self.show_time_stamp = True

    disable_time_stamp(self):
        self.show_time_stamp = False    
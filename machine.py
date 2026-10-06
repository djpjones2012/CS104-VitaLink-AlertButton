class Pin:
    IN = 0
    OUT = 1
    PULL_UP = 0
    PULL_DOWN = 1

    def __init__(self, id, mode=-1, pull=-1, value=1):
        self.id = id
        self.mode = mode
        self._value = value if value is not None else 0
        print(f"[Mock Machine] Initialized Pin {id} in mode {mode}")

    def value(self, val=None):
        if val is not None:
            self._value = val
            print(f"[Mock Machine] Pin {self.id} set to {val}")
        return self._value
    def on(self):
        self.value(1)

    def off(self):
        self.value(0)
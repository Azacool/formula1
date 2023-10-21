class TimeForm:
    def __init__(self,hour,minute,second,ms):
        self._hour=hour
        self._minute=minute
        self._second=second
        self._ms=ms

    def __str__(self) -> str:
        return f"{self._hour}:{self._minute}:{self._second}.{self._ms}"
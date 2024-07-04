# module to define api object and its porperties.

class API:
    def __init__(self) -> None:
        self.name = ""

    def __str__(self) -> str:
        if self.name:
            return f"{self.name} - API Object"
        else:
            return "API Object"
    

print(__name__)
# methods and classes for traders.
import pandas as pd


class Strategy:
    def __init__(self, strategy_name: str = None, data: pd.DataFrame = None) -> None:
        self.strategy_name = strategy_name
        self.description = "This is base strategy class!"
        pass

    def __repr__(self) -> str:
        return "Base strategy class"

    def __str__(self) -> str:
        if self.strategy_name is not None:
            return f"{self.strategy_name} : {self.description}"
        else:
            return "Base Strategy class"
        


if __name__ == "__main__":
    stgy = Strategy("Supertrend strategy")
    print(stgy)

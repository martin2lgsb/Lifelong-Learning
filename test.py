import pandas as pd

if __name__ == '__main__':
    file = pd.read_csv("./mathematics/symbol.csv", "\t")
    print(file)

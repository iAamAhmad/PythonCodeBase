import pandas as pd
import pandera as pa

l1 : list[int] = [1,2,3,4,5,6,7,8,9]
l1


s1 : pd.Series = pd.Series([1,2,3,4,5])
s1

s1 : pd.Series = pd.Series({"a": 10,
                            "b":20,
                            "c":30,
                            "d":40,
                            "e":50,
                            "f":60,
                            "g":70,})
s1


values : list[int] = [1, 2, 3, 4, 5]

index1 : list[list[str]] = [['a1', 'a1', 'a1', 'b1', 'b1'],
                            ['a', 'b', 'c', 'd', 'e']]

s1 : pd.Series = pd.Series(values, index=index1)
s1

values : list[int] = [1, 2, 3, 4, 5]

index1 : list[list[str]] = [['a1', 'a1', 'a1', 'b1', 'b1'],
                            ['a', 'b', 'c', 'd', 'e']]

s1 : pd.Series = pd.Series(values, index=index1, name="Student_Data")
s1
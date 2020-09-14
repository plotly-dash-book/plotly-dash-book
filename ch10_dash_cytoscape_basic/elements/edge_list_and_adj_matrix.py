import numpy as np
import pandas as pd

print("(1) タプルのリストによるエッジリスト")
edge_list = [("A", "B"), ("A", "C"), ("C", "D")]
print(edge_list)

print("\n(2) pandasのデータフレームによるエッジリスト(sourceは始点ノード、targetは終点ノード）")
pandas_edge_list = pd.DataFrame({"source": ["A", "B", "C"], "target": ["B", "C", "D"]})
print(pandas_edge_list)

# 隣接行列
print("\n(3) リストのリストによる隣接行列（ノード名は持てない）")
adj_matrix = [[0, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0]]
print(adj_matrix)

print("\n(4) pandasのデータフレームによる隣接行列（ノード名を持てる）")
pandas_adj_matrix = pd.DataFrame(
    [[0, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0]],
    index=["A", "B", "C", "D"],
    columns=["A", "B", "C", "D"],
)
print(pandas_adj_matrix)

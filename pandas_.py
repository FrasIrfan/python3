import pandas as pd

my_file = pd.DataFrame([[10, 20, 30], [40, 50, 60], [70, 80, 90]],
                       ['row1', 'row2', 'row3'], ['col1', 'col2', 'col3'], )
print(my_file)

# my_file_1 = pd.Series([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
# print(my_file_1)

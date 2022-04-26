import pandas as pd
import sys


def join_csv(path1, path2, column_name, join_type='left'):
    file1, file2 = pd.read_csv(path1), pd.read_csv(path2)
    file1.set_index(column_name)
    data = file1.join(file2.set_index(column_name), on=column_name, how=join_type)
    return data
    
print(join_csv(sys.argv[1], sys.argv[2], sys.argv[3]))



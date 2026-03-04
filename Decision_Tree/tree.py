import pandas as pd
import math
df = pd.read_csv("Decision_Tree/data.csv")

# So we know that we need to know on what feature is the dataset is being affected mostly to divide it into a tree like structure
# That we will call entropy


def entropy(y):
    total = len(y)
    
    count_0 = 0
    count_1 = 0
    
    for value in y:
        if value == 0:
            count_0 += 1
        else:
            count_1 += 1
    
    p0 = count_0 / total
    p1 = count_1 / total
    
    ent = 0
    
    if p0 != 0:
        ent -= p0 * math.log2(p0)
    if p1 != 0:
        ent -= p1 * math.log2(p1)
    
    return ent
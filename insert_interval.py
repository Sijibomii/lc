
#  [[1,2],[3,10],[12,16]]

"""
step 1: [[1,2],[3,5],[6,7],[8,10],[12,16], [4,8]] -sorting-> [[1,2],[3,5],[4,8],[6,7],[8,10],[12,16]]
"""
def insert_interval(intervals, newInterval):
    intervals.append(newInterval)
    out = []
    for i in sorted(intervals,  key=lambda i: i[0]):
        if out and out[-1][1] >= i[0]:
            out[-1][1] = max(i[1], out[-1][1])
        else:
            out.append(i)
    return out


print(insert_interval([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))

def merge(intervals):
    out = []
    for i in sorted(intervals, key=lambda i: i[0]):
        if out and i[0] <= out[-1][1]:
            # out is not empty and  the curr interval's start < last ineterval appended in out stop
            # merge
            out[-1][1] = max(out[-1][1], i[1])
        else:
            # just append that interval
            out.append(i)
    return out

# questions that can be solved with same technique
# https://leetcode.com/problems/non-overlapping-intervals/
# https://leetcode.com/problems/meeting-rooms-ii/
# https://leetcode.com/problems/meeting-rooms/
print(merge([[1,3],[2,6],[8,10],[15,18]]))
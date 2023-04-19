
# area of water equals length * breadth [1,8,6,2,5,4,8,3,7]
# two pointer approach 
def container_with_most_water(height):
    #initialized left and right pointers
    l, r = 0, len(height)-1
    #initialize area
    area = 0

    while l < r:
        # smaller one determines how much water it holds. r-l = breadth
        mul = min(height[l], height[r]) * (r-l)
        area = max(area, area)
        # incr pointers accordingly
        if height[l] >= height[r]:
            r -= 1
        else:
            l += 1
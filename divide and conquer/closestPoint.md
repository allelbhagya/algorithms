distance between two points p1 and p2 return

sqrt((p1.x - p2.x)^2 + (p1.y - p2.y)^2)

function closestPair(points):
n = number of points in the 'points' array

    # If there are less than 2 points, return a large value as the distance
    if n < 2:
        return infinity

    # Sort points based on their x-coordinate
    sort points by x-coordinate

    # Base case: If there are only two points, return their distance
    if n == 2:
        return distance(points[0], points[1])

    # Find the middle index
    mid = n / 2

    # Recursively find the closest pair in the left and right halves
    left_closest = closestPair(points[0:mid])
    right_closest = closestPair(points[mid:n])

    # Determine the smaller of the two closest distances
    min_distance = min(left_closest, right_closest)

    # Create a list to store the points that are within the strip of width 2*min_distance
    strip_points = []
    for each point in points:
        if abs(point.x - points[mid].x) < min_distance:
            strip_points.append(point)

    # Sort the points in the strip based on their y-coordinate
    sort strip_points by y-coordinate

    # Find the closest pair in the strip
    closest_in_strip = infinity
    for i from 0 to length of strip_points - 2:
        for j from i+1 to min(i+7, length of strip_points - 1):
            closest_in_strip = min(closest_in_strip, distance(strip_points[i], strip_points[j]))

    # Return the minimum distance among the three possibilities
    return min(min_distance, closest_in_strip)

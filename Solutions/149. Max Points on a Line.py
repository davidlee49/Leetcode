class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        #Intuition:
            #for each point O(n)
                #find all lines it makes with other points with line equation O(n)
                    #dict: key is line equation, value is count

        def get_line(point1, point2):
            # returns the (slope, y-intercept) for the 2 point line
            x1, y1, = point1
            x2, y2 = point2

            if x1 == x2:
                return (None, 0)

            m = (y2 - y1) / (x2 - x1)
            if m == 0:
                return (m, None)
            b = y1 - (m * x1)

            return (m, b)

        total_lines = {}

        # get 1st point
        for i, point1 in enumerate(points[:-1]):
            lines = {}
            # get 2nd point
            for point2 in points[i+1:]:
                # find line equation
                line = get_line(point1, point2)
                # check if equation is exist in total lines
                if line in total_lines:
                    continue
                elif line not in lines:
                    lines[line] = 2
                else:
                    lines[line] += 1
                # if not add to lines
            total_lines.update(lines)
        if len(points) == 1:
            return 1

        return max(total_lines.values())
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True

        (x0, y0), (x1, y1) = coordinates[0], coordinates[1]
        diffX = x1 - x0
        diffY = y1 - y0

        for x, y in coordinates[2:]:
            if ((x-x0)*diffY != diffX*(y-y0)):
                return False
        return True
import heapq


class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        adj = {}

        for src in points:
            adj[tuple(src)] = []

        for src in points:
            for dst in points:
                if(src != dst):
                    w = self.cost(src, dst)
                    adj[tuple(src)].append([w, tuple(dst)])

        
        heap_values = []
        visited = set()
        mst = []
        min_cost = 0

        for w, neighbour in adj[tuple(points[0])]:
            heapq.heappush(heap_values, [w, tuple(points[0]), neighbour])
        visited.add(tuple(points[0]))

        while len(heap_values) != 0:
            w, n1, n2 = heapq.heappop(heap_values)

            if n2 not in visited:
                visited.add(n2)
                mst.append([n1, n2])

                min_cost = min_cost + w

                for w, neighbour in adj[n2]:
                    if neighbour not in visited:
                        heapq.heappush(heap_values, [w, n2, neighbour])
        
        return min_cost
    
    def cost(self, pa, pb):
        distance= abs(pa[0] - pb[0]) + abs(pa[1] - pb[1])
        return distance

        
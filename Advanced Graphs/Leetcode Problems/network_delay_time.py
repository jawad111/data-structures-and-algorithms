import heapq


class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        adj = {}
        for edge in times:
            adj[edge[0]] = []
            adj[edge[1]] = []

        for src, dst, w in times:
            adj[src].append([w, dst])

        if(len(adj[k]) == 0):
            return -1

        heap_values = []
        max_heap_values = []
        visited = {}

        heapq.heappush(heap_values, [0, k])

        while len(heap_values) != 0:
            w1, n1 = heapq.heappop(heap_values)

            if n1 not in visited:
                heapq.heappush(max_heap_values, (-1 * w1, n1))
                visited[n1] = w1

                for w2, neighbour in adj[n1]:
                    if neighbour not in visited:
                        heapq.heappush(heap_values, [w1 + w2, neighbour])

        if(len(visited) == n):
            max, node =heapq.heappop(max_heap_values)
            return max * -1
        
        return -1
            
import heapq


def cheapest_flights(edges, source, destination, max_stops):
    adj = {}

    for src, dst, price in edges:
        adj[src] = []
        adj[dst] = []

    for src, dst, price in edges:
        adj[src].append([price, dst])

    print(adj)

    heap_values = []
    visited = {}
    stops = 0

    heapq.heappush(heap_values, [0, source])

    while len(heap_values) != 0:

        
    


        price, node = heapq.heappop(heap_values)

        

        if node is not visited:
            visited[node] = price
            

            if(node == destination):
                return price

        
            for price_neighbour , neighbour in adj[node]:
                if neighbour is not visited:
                    if(stops > max_stops):
                        price, node = heapq.heappop(heap_values)
                        return price
                    else:
                        heapq.heappush(heap_values, [price  + price_neighbour, neighbour])
        stops += 1
    
    return -1
    




n = 4
flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
src = 0
dst = 3
k = 1
print(cheapest_flights(flights, src, dst, k))
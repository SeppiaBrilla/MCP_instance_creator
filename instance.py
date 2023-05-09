from random import randint
import numpy as np
from datetime import datetime

class Instance:

    def __init__(self, m:'int', n:'int', max_load_range=(5,50)) -> None:
        self.m = m
        self.n = n
        self.max_load = self.get_max_loads(m, max_load_range, min_value= (max_load_range[0] * n))
        self.size = self.get_sizes(n, self.max_load)
        self.distances, self.optimal_paths = self.get_distances(self.max_load, self.size)
    
    def get_max_loads(self, m:'int', max_load_range:'tuple[int,int]', min_value:'int') -> list[int]:
        low = max_load_range[0]
        high = max_load_range[1]
        max_load = []
        max_load_sum = 0
        for i in range(m):
            val = randint(low, high)
            max_load.append(val)
            max_load_sum += val

        if min_value > max_load_sum:
            max_load = self.get_max_loads(m,max_load_range,min_value)
        return max_load
    

    def get_sizes(self, n:'int', max_sizes:'list[int]'):
        sizes = []
        m = len(max_sizes)
        remain = max_sizes.copy()
        for i in range(n):
            idx = randint(0,m - 1)
            while remain[idx] <= 0:
                idx = randint(0,m - 1)
            
            val = randint(1, remain[idx])
            remain[idx] -= val
            sizes.append(val)
        return sizes
    
    def get_distances(self, max_load: 'list[int]', size: 'list[int]'):
        n = len(size)
        m = len(max_load)
        distances = np.zeros(shape=(n + 1,n + 1))
        assignements = [[] for _ in range(m)]
        remaining_loads = max_load.copy()
        for i in range(n):
            courier = randint(0, m - 1)
            while remaining_loads[courier] < size[i]:
                courier = randint(0, m - 1)
            
            remaining_loads[courier] -= size[i]
            assignements[courier].append(i)
        for i in range(m):
            assiged = assignements[i]
            optimal = randint(1,5)
            distances[n, assiged[0]] = optimal
            distances[assiged[0], n] = optimal
            for j in range(1,len(assiged)):
                optimal = randint(1,5)
                current = assiged[j]
                distances[assiged[j - 1], current] = optimal
                distances[current, assiged[j - 1]] = optimal
        for i in range(n + 1):
            for j in range(n + 1):
                if distances[i,j] == 0:
                    distances[i,j] = randint(6,10)

        return distances, assignements
    

    def save_dzn(self):
        distaces_list = self.distances
        distaces_str_arr = [", ".join([str(int(i)) for i in distaces_list[j]]) for j in range(len(distaces_list))]
        distaces_str = '\n                      | '.join(distaces_str_arr)
        instance = f'''m = {self.m};
n = {self.n};
max_load = {self.max_load};
size = {self.size};
dist = [|{distaces_str}|]
% optimal assignement = {self.optimal_paths}
        '''
        file = open(f"instance_{self.m}_{self.n}_{datetime.today().isoformat()}.dzn", "x")
        file.write(instance)
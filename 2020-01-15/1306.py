arr = [4, 2, 3, 0, 3, 1, 2]
start = 5

length, visited = len(arr), set()
def dfs(i):
        if 0<=i<N and i not in visited:
            if arr[i]==0: return True
            visited.add(i)
            return dfs(i+arr[i]) or dfs(i-arr[i])
        return False
    return dfs(start)
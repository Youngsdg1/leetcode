arr = [4, 2, 3, 0, 3, 1, 2]
start = 5

def game(arr, start):

    def plus_current(index):
        return index + arr[index]
    
    def minus_current(index):
        return index - arr[index]
    
    def is_range(li, index):
        return 0 <= index < len(li)

    queue= []
    start_plus = plus_current(start)
    start_minus = minus_current(start)ddddddd
    if is_range(arr, start_plus):
        queue.append(start_plus)
    if is_range(arr, start_minus):
        queue.append(start_minus)
    while queue:
        for _ in range(2):
            a = queue.pop()
            a_plus = plus_current(a)
            a_minus = minus_current(a)
            if is_range(arr, a_plus):
                if arr[a_plus] == 0:
                    return True
                queue.append(a_plus)
            if is_range(arr, a_minus):
                if arr[a_minus] == 0:
                    return True
                queue.append(a_minus)
    return False


# %%
import queue
 # %%
pq = queue.PriorityQueue()
pq.put((2, 'B'))
pq.put((1, 'A'))
pq.put((5, 'E'))
pq.put((10, 'J'))

def change_priority(pq, z_old, z_new):
    new_pq = queue.PriorityQueue()
    while not pq.empty():
        curr_z, curr_val = pq.get()
        if curr_z == z_old:
            new_pq.put((z_new, curr_val))
        else:
            new_pq.put((curr_z, curr_val))
    return new_pq
    
pq = change_priority(pq, 5, 6)
# %%
while not pq.empty():
    print(pq.get())
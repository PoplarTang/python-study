import multiprocessing

queue = multiprocessing.Queue(3)

queue.put(123)
queue.put("hello")
queue.put([1,2,3])

print("empty: ",queue.empty())
print("full: ",queue.full())


print("queue.qsize(): ", queue.qsize())

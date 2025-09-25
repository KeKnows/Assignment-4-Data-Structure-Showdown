#1
def has_duplicates(product_ids):
    return len(product_ids) != len(set(product_ids))    
#A set is the best choice here because it automatically removes duplicates.
#The main operation is converting the list to a set, which runs in O(n) time, 
#and then comparing lengths, which is O(1). This makes it efficient for duplicate detection.


#2
class TaskQueue:
    def __init__(self):
        from collections import deque
        self._q = deque()
    def add_task(self, task):
        self._q.append(task)
    def remove_oldest_task(self):
        if not self._q:
            return None
        return self._q.popleft()
#A deque (double-ended queue) is ideal for queue-like behavior because it 
#supports O(1) insertion at the end and O(1) removal from the front. 
#The operations performed are enqueue (append) and dequeue (popleft).


#3
class UniqueTracker:
    def __init__(self):
        self._seen = set()
    def add(self, value):
        self._seen.add(value)
    def get_unique_count(self):
        return len(self._seen)
#A set is the most appropriate structure since it stores unique values by definition. 
#The operations are insertion (add) and counting the number of unique items (len), 
#both of which run in O(1) average time. 

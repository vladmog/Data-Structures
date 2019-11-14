from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.storage = dict()
        self.order = DoublyLinkedList()


    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # key present
        if key in self.storage:
            node = self.storage[key]
            self.order.move_to_end(node)
            return node.value[1]
        else:
            return None
        # key not present

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        #cases to handle

        # does the key already exist in the cache?
        if key in self.storage:
            #key is here so we should replace the value
            node = self.storage[key]
            node.value = (key, value)
            self.order.move_to_end(node)
            return
        # yes - 


        # no -
        # are we at a cap or not?
        # yes -
        if self.size == self.limit:
            # Dump the oldest item
            # delete the key value
            del self.storage[self.order.head.value[0]]
            # remove from head
            self.order.remove_from_head()
            # del self.storage[self.order.remove_from_head().value[0]]
            # subtract from count
            self.size -= 1
        # no -
        
        # how do we put stuff into the cache
        # if cache not full and key not present
        self.order.add_to_tail((key, value))
        self.storage[key] = self.order.tail
        self.size += 1


        

        


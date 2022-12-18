import rpyc
from constRPYC import *  # -
from rpyc.utils.server import ThreadedServer

# Expose the following list methods
#
# Method    | Description
# ----------+------------
# append()  | Adds an element at the end of the list
# clear()   | Removes all the elements from the list
# copy()    | Returns a copy of the list
# count()   | Returns the number of elements with the specified value
# extend()  | Add the elements of a list (or any iterable), to the end of the current list
# index()   | Returns the index of the first element with the specified value
# insert()  | Adds an element at the specified position
# pop()     | Removes the element at the specified position
# remove()  | Removes the first item with the specified value
# reverse() | Reverses the order of the list
# sort()    | Sorts the list


class DBList(rpyc.Service):
    value = []

    def exposed_value(self):
        return self.value

    def exposed_append(self, data):
        self.value = self.value + [data]
        return self.value

    def exposed_clear(self):
        self.value.clear()
        return self.value

    def exposed_copy(self):
        return self.value.copy()

    def exposed_count(self, n):
        return self.value.count(n)

    def exposed_extend(self, data):
        self.value.extend(data)
        return self.value

    def exposed_index(self, n):
        return self.value.index(n)

    def exposed_insert(self, pos, data):
        self.value.insert(pos, data)
        return self.value

    def exposed_pop(self, pos):
        self.value.pop(pos)
        return self.value

    def exposed_remove(self, n):
        self.value.remove(n)
        return self.value

    def exposed_reverse(self):
        self.value.reverse()
        return self.value

    def exposed_sort(self):
        self.value.sort()
        return self.value


if __name__ == "__main__":
    server = ThreadedServer(DBList(), port=PORT)
    server.start()

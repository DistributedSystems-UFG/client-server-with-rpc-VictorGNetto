import rpyc
from constRPYC import *  # -


class Client:
    conn = rpyc.connect(SERVER, PORT)  # Connect to the server

    print("exposed_value\n", conn.root.exposed_value(), "\n")

    conn.root.exposed_append(6)
    conn.root.exposed_append(5)
    conn.root.exposed_append(6)
    print("exposed_append\n", conn.root.exposed_value(), "\n")

    copy = conn.root.exposed_copy()
    print("exposed_copy\n", copy, "\n")

    print("exposed_count\n", conn.root.exposed_count(6), "\n")

    conn.root.exposed_extend([7, 7, 8, 9, 9, 9])
    print("exposed_extend\n", conn.root.exposed_value(), "\n")

    print("exposed_index\n", conn.root.exposed_index(8), "\n")

    conn.root.exposed_insert(1, 5)
    print("exposed_insert\n", conn.root.exposed_value(), "\n")

    conn.root.exposed_pop(1)
    print("exposed_pop\n", conn.root.exposed_value(), "\n")

    conn.root.exposed_remove(8)
    print("exposed_remove\n", conn.root.exposed_value(), "\n")

    conn.root.exposed_reverse()
    print("exposed_reverse\n", conn.root.exposed_value(), "\n")

    conn.root.exposed_sort()
    print("exposed_sort\n", conn.root.exposed_value(), "\n")

    conn.root.exposed_clear()
    print("exposed_clear\n", conn.root.exposed_value(), "\n")
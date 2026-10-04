"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """
    # BFS explores a graph one level at a time, visiting each adjacent node
    # before reaching out to their adjacent nodes on the next level. DFS
    # follows a path until it reaches the end before backing up and
    # exploring a different path.
    #
    # Exit the function safely when the start node is not present.
    if start not in graph:
        return []

    # The next_queue keeps track of which nodes need to be
    # visited and in what order. FIFO to traverse in the
    # order the nodes were discovered.
    next_queue = deque([(start, 0)])
    # Visited is a set to avoid any duplication.
    visited = set()
    order = []

    while next_queue:
        # Using deque.popleft() to ensure we are getting nodes in order.
        current, degree = next_queue.popleft()
        # Make sure the current node has not been visited already.
        if current not in visited:
            visited.add(current)
            # The tuple allows me to track the degree of each node.
            order.append((current, degree))
            for adjacent in graph.get(current, []):
                # Neighbors have to be added to the queue to ensure the function
                # is actually progressing through the graph and exploring each edge.
                next_queue.append((adjacent, degree + 1))

    return order


def main():

    # A quick helper function to show the pages, their level, and an arrow
    # to show the progression of the traversal.
    def print_helper(bfs_traversal):
        i = 0
        for page, degree in bfs_traversal:
            if i == 0 or i % 5:
                print(f"{page} ({degree})", end=" -> " if i < len(bfs_traversal) -1 else "\n")
            else:
                print(f"\n{page} ({degree})", end=" -> " if i < len(bfs_traversal) -1 else "\n")
            i += 1
        return

    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    print("\n=== GRAPH STRUCTURE ===\n")
    print("Create an adjacency list of wikipedia pages.")

    # I wanted to represent wikipedia links as an adjacency list,
    # went a little overboard. Each vertex represents a page and
    # each edge represents a link.
    wiki_link_graph = {
        'Bill Gates': ['Microsoft', 'Paul Allen', 'Seattle'],
        'Microsoft': ['Redmond', 'Bill Gates', 'Paul Allen', 'Windows'],
        'Paul Allen': ['Bill Gates', 'Microsoft', 'Seahawks', 'Hodgkin lymphoma'],
        'Windows': ['Microsoft', 'Operating System'],
        'Operating System': ['Windows', 'Linux'],
        'Linux': ['Operating System'],
        'Hodgkin lymphoma': ['Paul Allen', 'Marcello Malpighi'],
        'Marcello Malpighi': ['Hodgkin lymphoma'],
        'Seahawks': ['Seattle', 'Paul Allen', 'Osprey'],
        'Seattle': ['Bill Gates', 'Seahawks'],
        'Redmond': ['Microsoft'],
        'Osprey': ['Seahawks', 'Piscivore'],
        'Piscivore': ['Osprey']
    }

    print("A graph representing wikipedia pages and their links.")
    for page, link in wiki_link_graph.items():
        print(f"{page} -> {link}")

    # ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.

    print("\n=== BFS TRAVERSAL ===\n")

    print("Starting BFS traversal starting from Redmond. Degree from start displayed next to each page.")
    # BFS starts by visiting the first node, Redmond in this case. It keeps track
    # of each node that has been visited so that there are no repeats. It then
    # checks to see all adjacent nodes to the current node and adds them to the
    # deque. The while loop keeps iterating as long as there are nodes in the
    # deque and pops each node from the left to maintain the FIFO behavior,
    # ensuring that nodes are traversed level by level.
    bfs_order = bfs(wiki_link_graph, 'Redmond')
    print_helper(bfs_order)

    # Demonstrating adding a node and edge to the graph.
    print("\nAdding node \"Fishing spider\" to the traversal...")

    # Adding the edge from Piscivore to Fishing spider.
    wiki_link_graph['Piscivore'].append('Fishing spider')
    # Adding the vertex Fishing spider and setting the edge to Piscivore.
    wiki_link_graph['Fishing spider'] = ['Piscivore']

    print('Reprinting the traversal with the updated node, starting from Redmond again.')
    print_helper(bfs(wiki_link_graph, 'Redmond'))


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===\n")

    # Edge case 1 ==========================================================
    # Starting from a different node should not change the function's behavior.
    print(f"Working from a different start node: Piscivore")
    edge_case_1 = bfs(wiki_link_graph, 'Piscivore')
    print_helper(edge_case_1)

    # Edge case 2 ==========================================================
    # Traversing a disconnected graph should not include disconnected nodes.
    #
    # The function checks for adjacent nodes and never finds the disconnected
    # node and therefore never visits that node, returning an order list without
    # that entry.
    print("\nTesting traversal using a disconnected graph. Creating graph...")
    disconnected_graph = {
        'Page 1': ['Page 2'],
        'Page 2': ['Page 1'],
        'Page 3': []
    }
    print(f"Created graph: {disconnected_graph}")
    print("Traversing a disconnected graph.")
    edge_case_2 = bfs(disconnected_graph, 'Page 1')
    print_helper(edge_case_2)

    # Edge case 3 ==========================================================
    # Exiting safely when using a start node that is not in the graph.
    #
    # The bfs function always starts by checking if the node is in the
    # graph, returning an empty order list when it is not present to
    # avoid any exceptions.
    print("\nHandling a missing start node: Steve Jobs")
    edge_case_3 = bfs(wiki_link_graph, 'Steve Jobs')
    print(f"BFS call returned: {edge_case_3}")

    # Edge case 4 ==========================================================
    # Traversing a single node graph should return only the one node.
    #
    # The bfs function checks for any adjacent nodes and finds none,
    # no nodes are added to the deque so the while loop exits after
    # a single iteration and returns the order list.
    print("\nTraversing a single node graph. Creating graph...")
    single_node_graph = {'Single': []}
    print(f"Created graph: {single_node_graph}\nTraversing...")
    edge_case_4 = bfs(single_node_graph, 'Single')
    print_helper(edge_case_4)

    # Edge case 5 ==========================================================
    # Traversing an empty graph should return an empty order list.
    #
    # The bfs function is called but there are no keys in the
    # dictionary so it functions just like in edge case 3 with
    # the missing start node, returning an empty order list.
    print("\nTraversing an empty graph. Creating graph...")
    empty_graph = {}
    print(f"Created graph: {empty_graph}\nTraversing...")
    edge_case_5 = bfs(empty_graph, 'Start')
    print_helper(edge_case_5)



if __name__ == "__main__":
    main()
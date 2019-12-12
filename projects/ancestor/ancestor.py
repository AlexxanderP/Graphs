
from collections import deque

def earliest_ancestor(ancestors, starting_node):
    family_tree = {}
    for (parent, child) in ancestors:
        # If the child's already there, add the parent
        if child in family_tree:
            family_tree[child].append(parent)
        # Otherwise, create the child with the parent
        else:
            family_tree[child] = [parent]
    # Initialize tracking variables
    ancestor = starting_node
    generations = 0
    # Initialize stack
    stack = deque([(ancestor, generations)])
    while len(stack) > 0:
        # Grab next potential child from stack
        (child, child_generations) = stack.pop()
        # If they're a new earliest ancestor, set them as such
        if child_generations > generations:
            ancestor = child
            generations = child_generations
        # If they're equal generations back but have a smaller ID, set them as the new earliest ancestor
        elif child_generations == generations and child < ancestor:
            ancestor = child
        # If the child has known parents...
        if child in family_tree:
            # Extend the stack with their parents and the generations increased by 1
            stack.extend([(parent, child_generations + 1) for parent in family_tree[child]])
    
    return -1 if generations == 0 else ancestor 
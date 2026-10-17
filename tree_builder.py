class EmployeeNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class TeamTree:
    def __init__(self):
        self.root = None

    def insert(self, manager_name, employee_name, side, current_node=None):
        # Normalize manager name for comparison
        manager_name = manager_name.strip().lower()

        # Start at root if no node provided
        if current_node is None:
            current_node = self.root

        # No root exists
        if current_node is None:
            print("❌ No team lead exists yet. Add a root first.")
            return False

        # Found the manager (case-insensitive)
        if current_node.name.strip().lower() == manager_name:
            side = side.strip().lower()

            if side == "left":
                if current_node.left is None:
                    current_node.left = EmployeeNode(employee_name)
                    print(f"✅ {employee_name} added to the LEFT of {current_node.name}")
                    return True
                else:
                    print(f"❌ LEFT side of {current_node.name} is already occupied.")
                    return False

            elif side == "right":
                if current_node.right is None:
                    current_node.right = EmployeeNode(employee_name)
                    print(f"✅ {employee_name} added to the RIGHT of {current_node.name}")
                    return True
                else:
                    print(f"❌ RIGHT side of {current_node.name} is already occupied.")
                    return False

            else:
                print("❌ Side must be 'left' or 'right'.")
                return False

        # Search left subtree
        if current_node.left:
            if self.insert(manager_name, employee_name, side, current_node.left):
                return True

        # Search right subtree
        if current_node.right:
            if self.insert(manager_name, employee_name, side, current_node.right):
                return True

        # Manager not found in this branch
        return False

    def print_tree(self, node=None, level=0):
        if node is None:
            if level == 0:
                node = self.root
                if node is None:
                    print("❌ No team lead exists yet.")
                    return
            else:
                return

        print("  " * level + f"- {node.name}")

        self.print_tree(node.left, level + 1)
        self.print_tree(node.right, level + 1)


"""
===========================
      DESIGN MEMO
===========================
Implementing recursive insertion in the company directory helped me understand how trees naturally model hierarchical relationships. 
The insertion process works by starting at the root and recursively exploring the left and right branches until the correct manager node is found. 
Each recursive call receives a smaller portion of the tree, and once the manager’s name matches the current node, the new employee is attached to either the left or right pointer. 
The function then returns a success value that propagates back up the recursive chain, signaling that the insertion is complete. 
This approach eliminates the need for loops and makes the structure easy to navigate.
One of the main challenges I faced was ensuring that the program actually found the correct spot for a new employee. 
Early versions of my code failed silently when the manager was added, which feels backwards to admit, but what would happen is I would add the manager and the program would never document the manager insertion.
For example, I'd include a Riley as the manager, then her employees, Tim and Tom (Original I know).
It would fail to list them when I used the prompt and also failed to list the employees in the first place. 
Had to implement a whole new section for the employees, as in rewrite the sections related to adding instances.
I felt dumb for about 10 minutes. I also realize this part was less professionally written, but I wanted to make it known what part was the most trouble whether I like it or not. 
At least I knew Binary Trees from my time with C++.
Fixing this required adding return values to the recursive calls and checking them in the CLI so the program could report when a manager wasn’t found. 
Another challenge was preventing accidental overwriting of the team lead, which required adding a guard before assigning the root.
Trees are preferable to other data structures when data has a clear parent‑child relationship. 
Organizational charts, file systems, website DOM structures, and decision trees all rely on hierarchical organization. 
In these cases, trees make searching, inserting, and visualizing relationships more intuitive and efficient than flat structures like lists or dictionaries.
"""

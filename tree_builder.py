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


"""

from tree_builder import TeamTree, EmployeeNode

def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")

        choice = input("Choose an option (1–4): ")

        # Add team lead
        if choice == "1":
            name = input("Enter team lead's name: ")

            if tree.root is not None:
                print("❌ A team lead already exists. Reset the tree before adding a new one.")
                continue

            tree.root = EmployeeNode(name)
            print(f"✅ {name} added as the team lead.")

        # Add employee
        elif choice == "2":
            if tree.root is None:
                print("❌ You must add a team lead first.")
                continue

            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ").lower()

            success = tree.insert(manager, employee, side)

            if not success:
                print(f"❌ Manager '{manager}' not found in the team.")

        # Print tree
        elif choice == "3":
            print("\n🌳 Current Team Structure:")
            tree.print_tree()

        # Exit
        elif choice == "4":
            print("Good Bye!")
            break

        else:
            print("❌ Invalid option. Choose 1–4.")

if __name__ == "__main__":
    company_directory()

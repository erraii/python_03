import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    total_arguments = len(sys.argv)
    arguments_received = total_arguments - 1
    if (total_arguments < 2):
        print("No arguments provided!")
    else:
        i = 1
        print(f"Arguments received: {arguments_received}")
        for arg in sys.argv[1:]:
            print(f"Argument {i}: {arg}")
            i += 1
    print(f"Total arguments: {total_arguments}")

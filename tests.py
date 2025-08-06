from functions.get_files_info import *

def main():
    print(get_files_info("calculator", "."), '\n')

    print(get_files_info("calculator", "pkg"), '\n')

    print(get_files_info("calculator", "/bin"), '\n')

    print(get_files_info("calculator", "../"))

if __name__ == "__main__":
    main()

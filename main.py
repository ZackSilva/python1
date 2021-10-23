if __name__ == '__main__':
    import platform
    # This function displays information about the current computer hardware information etc.
    def demonstrate_module():
        print(f"Python version: {platform.python_version()}")
        print(f"Machine architecture: {platform.architecture()}")
        print(f"Machine processor type: {platform.processor()}")

    demonstrate_module()


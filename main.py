if __name__ == '__main__':
    import re
    import os
    txt = "Windows"
    print(re.search(os.uname(sysname), txt))
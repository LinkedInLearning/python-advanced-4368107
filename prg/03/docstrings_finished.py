# Demonstrate the use of function docstrings


def myFunction(arg1, arg2=None):
    """myFunction(arg1, arg2=None) --> 実際には何もせず、出力するだけ

    Parameters:
    arg1: 1番目の引数
    arg2: 2番目の引数。デフォルトはNone
    """
    print(arg1, arg2)


def main():
    print(myFunction.__doc__)


if __name__ == "__main__":
    main()

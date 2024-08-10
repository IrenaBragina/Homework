from math import inf
def divide(first,second):
    if second == 0:
        return inf
    return first/second
if __name__ == "__main__":
    print(divide(50,5))
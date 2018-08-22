from collections import deque

def search(lines, pattern, history=5):
    previous_line = deque(maxlen=history)
    for li in lines:
        if pattern in li:
            yield li, previous_line
        previous_line.append(li)


if __name__ == '__main__':
    with open("somefile.txt") as f:
        for line, previous in search(f, "python", 5):
            for pre in previous:
                print("pre:" + pre)
            print("line:" + line)
            print("-----------")
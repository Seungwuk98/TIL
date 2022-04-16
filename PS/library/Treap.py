from random import randint


class Node:
    def __init__(self, val) -> None:
        self.cnt = 1
        self.sum = self.val = val
        self.pri = randint(1, 100000000)
        self.l = self.r = self.p = None

    def update(self):
        self.cnt = 1
        self.sum = self.val
        if self.l:
            self.sum += self.l.sum
            self.cnt += self.l.cnt
        if self.r:
            self.sum += self.r.sum
            self.cnt += self.r.cnt


class Treap:
    def __init__(self) -> None:
        self.tree = None

    def split(self, x, k):
        p = x
        print(p)
        lroot = rroot = x
        if k <= x.val:
            while x.l and k <= x.l.val:
                print(1)
                x = x.l
            lroot = x.l
            if x.l:
                x.l.p = None
                x.l = None
        else:
            while x.r and k > x.r.val:
                print(2)
                x = x.r
            rroot = x.r
            if x.r:
                x.r.p = None
                x.r = None
        while x != p.p:
            print(3)
            x.update()
            x = x.p
            print(x)
        return lroot, rroot

    def insert(self, val):
        y = Node(val)
        if not self.tree:
            self.tree = y
            return
        x = self.tree
        while True:
            print(4)
            if x.pri < y.pri:
                y.p = x.p
                if not x.p:
                    self.tree = y
                elif x.p.l == x:
                    x.p.l = y
                else:
                    x.p.r = y
                lroot, rroot = self.split(x, y.val)
                y.l = lroot
                y.r = rroot
                if y.l:
                    y.l.p = x
                if x.r:
                    y.r.p = x
                break
            if val <= x.val:
                if not x.l:
                    x.l = y
                    y.p = x
                    break
                x = x.l
            else:
                if not x.r:
                    x.r = y
                    y.p = x
                    break
                x = x.r
        while y:
            print(5)
            y.update()
            y = y.p

    def kth(self, k):
        x = self.tree
        while True:
            print(6)
            while x.l and x.l.cnt > k:
                print(7)
                x = x.l
            if x.l:
                k -= x.l.cnt
            if not k:
                break
            k -= 1
            x = x.r
        return x.val


treap = Treap()

for i in range(int(input())):
    treap.insert(int(input()))
    print(treap.kth(i >> 1))

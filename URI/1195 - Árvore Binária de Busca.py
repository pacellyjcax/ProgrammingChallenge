class BSTNode(object):
 
    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def add(self, key):
        side = 'left' if key < self.key else 'right'
        node = getattr(self, side)
        if node is None:
            setattr(self, side, BSTNode(key))
        else:
            node.add(key)
 
    def remove(self, key):
        if key < self.key:
            self.left = self.left.remove(key)
        elif key > self.key:
            self.right = self.right.remove(key)
        else:
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right

            tmp = self.right._min()
            self.key, self.value = tmp.key, tmp.value
            self.right._remove_min()
        return self
 
    def _min(self):
        if self.left is None:
            return self
        else:
            return self.left._min()
 
    def _remove_min(self):
        if self.left is None:  
            return self.right
        self.left = self.left._removeMin()
        return self

    def traverse(self, order='pre'):
        global pre, inn, pos
        if order == 'pre':
            pre.append(self.key)
        if self.left is not None:
            self.left.traverse(order)
        if order == 'in':
            inn.append(self.key)
        if self.right is not None:
            self.right.traverse(order)
        if order == 'post':
            pos.append(self.key)


if __name__ == '__main__':
    n = int(raw_input())
    for i in xrange(n):
        raw_input()
        v = [int(x) for x in raw_input().split()]
        tree = BSTNode(v[0])
        if len(v)>1:
            for j in xrange(1,len(v)):
                tree.add(v[j])
        pre = []
        inn = []
        pos = []
        tree.traverse('pre')
        tree.traverse('in')
        tree.traverse('post')
        vpre = str(pre)
        vpre = vpre.replace("[","")
        vpre = vpre.replace("]","")
        vpre = vpre.replace(",","")
        vinn = str(inn)
        vinn = vinn.replace("[","")
        vinn = vinn.replace("]","")
        vinn = vinn.replace(",","")
        vpos = str(pos)
        vpos = vpos.replace("[","")
        vpos = vpos.replace("]","")
        vpos = vpos.replace(",","")
        print '''Case {0:d}:
Pre.: {1:s}
In..: {2:s}
Post: {3:s}'''.format(i+1,vpre,vinn,vpos)
        print

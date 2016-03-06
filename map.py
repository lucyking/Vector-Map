# coding=utf-8
import random, sys
import optparse

BRANCH = 8
NODE = 600
MIN = 0


class Alpha(object):
    branch = BRANCH
    node = NODE
    min_branch = MIN

    def __init__(self):
        self.options = self.parse_option()
        if self.options.branch:
            self.branch = int(self.options.branch)
            # print self.options.branch
        if self.options.node:
            self.node = int(self.options.node)

    def parse_option(self):
        opt = optparse.OptionParser()
        opt.add_option('-x', '--xseq', metavar='true', default='false',
                       help='gen break index list')
        opt.add_option('-b', '--branch', metavar='N', default=8,
                       help='set branch number')
        opt.add_option('-n', '--node', metavar='M', default=600,
                       help='set nodes number')
        opt.add_option('--min', metavar='Num', default=0,
                       help='set min vector,min<=branch')
        options, arguments = opt.parse_args()
        return options

    def gen_list(self):
        list = map(lambda x: random.randint(0, self.node), xrange(self.node))
        list.sort()
        list = self.uniq(list)
        b = []
        for i in list:
            if i not in b:
                b.append(i)
        b.sort()
        return b

    def gen_leaner_list(self):
        return xrange(random.randint(2, self.node))

    def uniq(self, list):
        b = []
        for i in list:
            if i not in b:
                b.append(i)
        b.sort()
        return b


if __name__ == '__main__':
    Alpha = Alpha()

    if Alpha.options.xseq == 'true':
        list = Alpha.gen_list()
    elif Alpha.options.xseq == 'false':
        list = Alpha.gen_leaner_list()
    else:
        sys.exit()

    if Alpha.options.min:
        Alpha.min_branch = int(Alpha.options.min)
        if int(Alpha.options.min)>int(Alpha.options.branch):
            print 'int(min) should <= int(branch)'
            sys.exit()
        # print '>>>min', int(Alpha.options.min)

    index = 0
    for v in list:
        if Alpha.options.xseq == 'true':
            list_tmp = xrange(random.randint(0, Alpha.branch))  # gen des_list[>length<]
        else:
            list_tmp = xrange(random.randint(Alpha.min_branch, Alpha.branch))
        # print list_tmp
        list_des = map(lambda x: random.randint(0, Alpha.node), list_tmp)  # gen des_list[>index<]
        # print list_des
        # list_des = Alpha.uniq(list_des)

        for k in list_des:
            if k != v:
                print str(index) + ',' + str(v) + ',' + str(k) + ',' + str(random.randint(1, 20))
                index += 1

    # print 'Node:', len(list),'|',
    # print 'vector:', index,'|',
    # print 'Break-sequence:', Alpha.options.xseq

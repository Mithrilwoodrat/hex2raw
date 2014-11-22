#author : mithrilwoodrat
# -*- coding: utf-8 -*-
import sys


sys.out.write(reduce(lambda x,y:x+y,
                     [chr(int(i,16)) for i in
                      sys.stdin.readline().split()])

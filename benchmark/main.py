# Copyright 2012 Jeffrey R. Spies
# License: Apache License, Version 2.0
# Website: http://jspi.es/benchmark

from . import __VERSION__
from Benchmark import Benchmark

import time
import platform
import os
import sys
import inspect

class BenchmarkProgram(object):
    
    benchmarks = []

    def __init__(self, module="__main__", **kwargs):
        if isinstance(module, basestring):
            self.module = __import__(module)
        else:
            self.module = module
    

    def run(self, *args, **kwargs):
        if len(self.benchmarks) < 1:
            self.benchmarks = self.loadFromModule(self.module)
        
        totalRuns = 0
        objects = []
        
        for obj in self.benchmarks:
            obj = obj(**kwargs)
            obj.run()
            objects.append(obj)
            totalRuns += obj.getTotalRuns()
        
        title = 'Benchmark Report'
        info = 'Each of the above %s runs were run in random, non-consecutive order' % str(totalRuns)
        sys.stdout.write(self.printMarkdown(objects, title, info, **kwargs))


    def printMarkdown(self, benchmarks, title, info, **kwargs):
        lines = ''

        lines += os.linesep
        lines += title
        lines += os.linesep + '='*len(title)
        lines += os.linesep*2
        
        for obj in benchmarks:
            if obj.label:
                title = obj.label
            else:
                title = obj.__class__.__name__
                title = title.replace('_', ' ')
            
            labelLength = len(title) if len(title) > 5 else 5
            lines += title
            lines += os.linesep
            lines += '-'*labelLength
            lines += os.linesep*2
            
            lines += obj.getTable(**kwargs)
            lines += os.linesep*2
        
        lines += info
        lines += os.linesep*2

        return lines
        
    def loadFromModule(self, module, exclude=()):
        if isinstance(module, basestring):
            module = __import__(module)
        else:
            module = module
        for name, member in inspect.getmembers(module):
            obj = getattr(module, name)
            if isinstance(obj, type) and issubclass(obj, Benchmark) and name not in exclude:
                self.benchmarks.append(obj)

main = BenchmarkProgram
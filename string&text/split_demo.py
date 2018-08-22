#!/usr/bin/env python3
# coding=utf-8

import re

line = 'asdf fjdk; afed, fjek,asdf, foo'


b = re.split(r'[,;\s]\s*', line)

print(b)


c = re.split(r'(;|,|\s)\s*', line)

print(c)

#!/usr/bin/env Python
# -*- coding: utf-8 -*-

"""
@author: 陈 子坤 (GitHub@sandyzikun)
@time: 2022-03-18 23:39
"""

import sympy as sym

p1, p2, lamb, q1, q2, s, alph, beta = sym.symbols("p1 p2 lamb q1 q2 s alph beta")

L = (p1 ** alph) * (p2 ** beta) + lamb * (s - q1 * p1 - q2 * p2)

diff_p1, diff_p2, diff_lamb = sym.diff(L, p1), sym.diff(L, p2), sym.diff(L, lamb)

sln = sym.solve(
    [ diff_p1 , diff_p2 , diff_lamb ],
    [      p1 ,      p2 ,      lamb ]
    )

p1_solved, p2_solved, lamb_solved = sln[0]

print(sym.pretty(p1_solved)) # Also `.pretty_print(...)` or `.pprint(...)` of SymPy
print(sym.pretty(p2_solved))
print(sym.pretty(lamb_solved))

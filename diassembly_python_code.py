#!/usr/bin/env python3

# how interpreter works
"""
1. Lexing 
2. Parsing
3. Generate bytecode
4. Exec in PVM (python virtual machine)
"""

# read bytecode
import dis
def check(name):
 if name == "john":
   return "hello john"
 else:
   return "hello other"
bytecode = dis.dis(check)
print(bytecode)

"""
output :

  6           0 RESUME                   0

  7           2 LOAD_FAST                0 (name)
              4 LOAD_CONST               1 ('john')
              6 COMPARE_OP              40 (==)
             10 POP_JUMP_IF_FALSE        1 (to 14)

  8          12 RETURN_CONST             2 ('hello john')

 10     >>   14 RETURN_CONST             3 ('hello other')
"""

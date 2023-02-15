from transforms3d import *
from transforms3d.affines import *
from transforms3d.axangles import *
import numpy as np
from sympy import *

d1,d2,t3,l1,l2,t2,PI,l3,l4 = symbols("d1,d2,t3,l1,l2,t2,PI,l3,l4")
a,b,c,d,e,f,g,h,i=symbols('a,b,c,d,e,f,g,h,i')
A,B,C,D,E,F,G,H,I=symbols('A,B,C,D,E,F,G,H,I')

n1,n2,n3=symbols("n1,n2,n3")

def rot(axis,angle):
    kx,ky,kz=axis
    c=cos(angle)
    s=sin(angle)
    v=1-c
    return Matrix([
        [kx*kx*v+c     ,   kx*ky*v - kz*s,   kx*kz*v + ky*s,0],
        [kx*ky*v + kz*s,   ky*ky*v + c   ,   ky*kz*v - kx*s,0],
        [kx*kz*v - ky*s,   ky*kz*v+kx*s  ,   kz*kz*v+c,0     ],
        [0,0,0,1]])
def homo_rot(axis,angle):
    kx,ky,kz=axis
    c=cos(angle)
    s=sin(angle)
    v=1-c
    return Matrix([
        [kx*kx*v+c     ,   kx*ky*v - kz*s,   kx*kz*v + ky*s],
        [kx*ky*v + kz*s,   ky*ky*v + c   ,   ky*kz*v - kx*s],
        [kx*kz*v - ky*s,   ky*kz*v+kx*s  ,   kz*kz*v+c     ]
        ])

def homo_tran(vec):
    a,b,c = vec
    return Matrix([ [1,0,0,a],
                    [0,1,0,b],
                    [0,0,1,c],
                    [0,0,0,1]])
#simplify
def simp(ex1):
    ex2=ex1
    for a in preorder_traversal(ex1):
        if isinstance(a, Float):
            ex2 = ex2.subs(a, round(a, 1))
    return ex2

test1=Matrix([[a,b,c],[d,e,f],[g,h,i]])
test2=Matrix([[A,B,C],[D,E,F],[G,H,I]])

T=Matrix([[0.2,0.8],[0.1,0.9]])
R=Matrix([0,1])
T=Matrix([[0.9,0.1],[0.2,0.8]])
R=Matrix([0,1])
id=eye(2)
ans= (id - 0.9*T).inv()@R
pprint(ans)

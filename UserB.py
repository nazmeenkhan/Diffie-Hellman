import socket
import math
import random

c=socket.socket()
HOST= '127.0.0.1'
PORT = 5050
c.connect((HOST, PORT))
 

q = int(c.recv(1024))
alpha = int(c.recv(1024))
Xb = random.randint(1,q)
Yb=pow(alpha,Xb,q)
print("Yb: ", Yb)
Ya=int(c.recv(1024))
c.send(str(Yb).encode())
Kb=pow(Ya,Xb,q)
print("Symmetric Key: ",Kb)
c.close()














'''Xb=int(input("Enter Xb: "))
print("Xb :",Xb)
q = int(input("Enter a prime number: "))
num = 0
primitive_roots = []
for each in range(1, q):
	num += 1
	candidate_prim_roots = []
	for i in range(1, q):
		modulus = (num ** i) % q
		candidate_prim_roots.append(modulus)	
		cleanedup_candidate_prim_roots = set(candidate_prim_roots)
		if len(cleanedup_candidate_prim_roots) == len(range(1,q)):
			primitive_roots.append(num)
print ("Primitive roots of %d are:" % q)


print ("Primitive roots of %d are:" % q)
print (primitive_roots)
alpha=primitive_roots[0]
if Xb<q :
	Yb=(str((alpha**Xb)%q)).encode()
Ya=int(c.recv(1024))
print(Ya)
c.send(Yb)
Kb=(Ya**Xb)%q
print(Kb)'''
import socket
import math
import random

def prime():
    prime = 0
    while prime == 0:
        num = random.randint(2,99)

        for i in range(2, (num//2)): 
     
            if (num % i) == 0:
                 prime = 0
                 break
        else:
            prime = num 
            return prime
            break 

def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def root_calc():
	while True:
		q = prime()
		roots = []
		required_set = set(num for num in range (1, q) if gcd(num, q) == 1)
		for g in range(1, q):
			actual_set = set(pow(g, powers) % q for powers in range (1, q))
			if required_set == actual_set:
				roots.append(g)
				if len(roots)>10:
					break
			if len(roots) == 0:
				continue
			else:
				break
		return(q,random.choice(list(roots)))

q,alpha=root_calc()
print("prime no: ", q)
print("alpha: ",alpha)
Xa = random.randint(1,q)

server = socket.socket()
port=5050
server.bind(('127.0.0.1',port))
server.listen(10)
conn, address = server.accept()

conn.send(str(q).encode())
conn.send(str(alpha).encode())

Ya=pow(alpha,Xa,q)
print("Ya: ",Ya)
conn.send(str(Ya).encode())
Yb=int(conn.recv(1024))
Ka=pow(Yb,Xa,q)
print("Symmetric Key: ",Ka)

conn.close()
















'''Xa=int(input("Enter Xa: "))
print("Xa :",Xa)
q = int(input("Enter a prime number: "))
num= 0 
p_roots = []
for each in range(1, q):
	num += 1
	c_prim_roots = []
	for i in range(1, q):
		val = (num ** i) % q
		c_prim_roots.append(val)
		cleanedup_candidate_prim_roots = set(c_prim_roots)
		if len(cleanedup_candidate_prim_roots) == len(range(1,q)):
			p_roots.append(num)
print ("Primitive roots of %d are:" % q)
print (p_roots)
alpha=p_roots[0]

#conn.send(str(q)).encode()
#conn.send(str(p_roots)).encode()
if Xa<q:
	Ya=(str((alpha**Xa)%q)).encode()
conn.send(Ya)
Yb=int(conn.recv(1024))
print(Yb)
Ka=(Yb**Xa)%q
print(Ka)'''
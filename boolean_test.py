#! /usr/bin/env python
f = None

# Random no added in my case I have used 8 instead of the initial 5
# Git is getting on my nerves

for i in range(14):
	with open ("__application.log", "w") as f:
		if i>2:
			break
print("Does file exist and has been closed succcesfully : ", f.closed)
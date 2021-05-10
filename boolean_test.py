#! /usr/bin/env python
f = None

# Random no added in my case I have used 8 instead of the initial 5

for i in range(8):
	with open ("app_lica_tion.log", "w") as f:
		if i>2:
			break
print(f.closed)

#!/usr/bin/env python3
import base64, sys
try:
	with open(sys.argv[1],"rb") as f:
		print(base64.b64encode(f.read()).decode("utf8"))
except:
	print(f"""usage: {sys.argv[0]} FILE

Program will print the FILE's contents encoded
as base64.""")


#!/usr/bin/env python3

"""

	Cross post guff from my blog to my Tumblr
	Invoked with /path/to/blatt.py 'title' 'body'

"""

import pytumblr	#the tumblr API
from sys import argv	#body and title
from blattconf import *	#config file

client=pytumblr.TumblrRestClient(
	ck,
	cs,
	ot,
	os
)

client.create_text(
	blog,
	state="published",
	title=argv[1].replace(blagdir,""),
	body=(
		" ".join(argv[2:])
	)
)

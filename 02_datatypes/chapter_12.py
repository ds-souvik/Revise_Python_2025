'''Operations with Advanced datatypes'''

import arrow

store_time = arrow.utcnow()
convert_into_europe_tz = store_time.to("Europe/ Rome")

from collections import namedtuple

#Right now is not the right time to learn this. We will learn it later.
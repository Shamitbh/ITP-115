
import happybase

connection = happybase.Connection('localhost')
connection.open()

table = connection.table('resume')

# Read from text file line by line
# Google
# description
# 5
# responsibility 1
# responsibility 2
# responsibility 3
# responsibility 4
# responsibility 5


# Example:
# table.put(b'row-key', {b'family:qual1': b'value1',
#		  b'family:qual2': b'value2'})

# Example with our data:
# table.put(b'description@Google'), {b'job_info:responsiblity1: b'blahblah', b'job_info:responsiblity2: b'blahblahblah'})

rows = [
    (12345, 'abc'),
    (67890, 'def'),
    (87654, 'ghi')
]

output = open("/tmp/test.csv", 'w')
for row in rows:
    output.write("%d,%s\n" % (row[0], row[1]))
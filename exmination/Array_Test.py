a = "Python is beautiful"

print(a[0:5])

text = "Hello"
number = 10

result = "test %s %d" % (text, number)
print(result)

per = "%d%%" % number
print(per)

a = "%10s" % text
b = "%-10sjane" % text
print(a)
print(b)

c = "test {0} {1}".format(text, number)
print(c)



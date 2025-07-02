tag = '<a href="http://www.python.org">Python web site</a>'
print(tag)
print(tag[9:30])
print(tag[32:-4])


numbers = [1,2,3,4,5,6,7,8,9]
print(numbers)
print(numbers[0:2])
print(numbers[2:9])
print(numbers[2:-1])
print(numbers[2:-2])

#代码清单2-2是一个小程序，它提示用户输入一个URL，并从中提取域名。（这里假定输入的URL类似于http://www.somedomainname.com。）

url = input('Enter URL: ')
print("Domain name: " + domain)

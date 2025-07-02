# 方法append用于将一个对象附加到列表末尾。

list = [1,2,3,4]
list.append(5)
print(list)


#  方法clear就地清空列表的内容

list.clear()
print(list)

# 方法 copy 复制列表。前面说过，常规复制只是将另一个名称关联到列表。

# 方法count计算指定的元素在列表中出现了多少次。
print(['to', 'be', 'or', 'not', 'to', 'be'].count('to'))
# 方法extend让你能够同时将多个值附加到列表末尾，为此可将这些值组成的序列作为参数提
a = [1,2,3]
b = [4,5,6]
a.extend(b)
print(a)
# 供给方法extend。换而言之，你可使用一个列表来扩展另一个列表。

# 方法index在列表中查找指定值第一次出现的索引。

#方法insert用于将一个对象插入列表

# 方法pop从列表中删除一个元素（末尾为最后一个元素），并返回这一元素。  栈和队列
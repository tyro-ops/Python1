x = 1

# print(id(x))

x = x+1
# print(id(x))


y = [1, 2, 2, 3, 2]


# print(id(y))


y.append(6)

# print(id(y))

# print(y)
course = "python programing"
# print(len(course))
# print(course[0:3])
# print(course[0])
# print(course[0:2])
# print(course[:])
# print(id(course[0]))
# print(id(course))
message = "python \"programing"
# #message = """

# test is not easy
# testis very easy
# i am will give test

# """
# print(message)

# first = "Yogesh"
# last = "kalbhore"
# #full = first + " " + last
# full = f"{len(first)} {4+7}"
# print(full)
study = "  python programing   "
print(study.upper())
print(study.lower())
print(study.title())
print(study.strip())
print(study.lstrip())
print(study.rstrip())
print(study.rsplit())
print(study.split())
print(study.lstrip())
print(study.find("pro"))

msg = study.replace('p', 'j')
print(msg)
print("programing" not in study)

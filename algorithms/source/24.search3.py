
def search_list(a):
    if (a in stu_dic) is True:
        return stu_dic[a]
    else:
        return '?'

stu_no = [39, 14, 67, 105]

stu_name = ["Justin", "John", "Mike", "Summer"]

stu_dic ={39: "Justin", 14: "John", 67: "Mike", 105: "Summer"}

print(search_list(39))
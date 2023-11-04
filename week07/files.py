def split_name(file):
    number = "0123456789"
    others = " -."
    result = []
    head,num = -1,-1

    for i in range(len(file)):
        if file[i] in number and head ==-1:
            result.append(file[:i])
            head = i
        elif file[i] not in number and head!=-1 and num==-1:
            result.append(file[head:i])
            num=i
        elif file[i] in others and head!=-1 and num==-1:
            result.append(file[head:i])
            num = i
            break;

    if len(result) == 0:
        result.append(file)
        result.append([])
    elif len(result) == 1:
        result.append(file[head:])
    return result

def smaller(left,right):# left smaller : 0, right smaller : 1
    split_l = split_name(left)
    split_r = split_name(right)
    head = [split_l[0].lower(),split_r[0].lower()]
    num = [int(split_l[1]),int(split_r[1])]
    head_s = sorted(head)
    num_s = sorted(num)

    if head_s != head:
        return 1
    elif head[0]==head[1] and num_s != num:
        return 1
    else:
        return 2 if head[0]==head[1] and num[0]==num[1] else 0

def solution(files):
    for i in range(1,len(files)):#insertion sort
        for j in range(i,0,-1):
            if smaller(files[j],files[j-1])==0:
                files[j],files[j-1] = files[j-1],files[j]
            else:
                break;
    return files
def firstuniqchar(s):
    dic = {}
    for i in s:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    for key, value in dic.items():
        if value == 1:
            return s.index(key)
    return -1


if __name__ == "__main__":
    print(firstuniqchar("leetcode"))
    print(firstuniqchar("loveleetcode"))
    print(firstuniqchar("aavv"))

# -*- coding:utf-8 -*-
import codecs
str1 = "♠ ♣ ♦ ♥ ♠ ♣ ♦ ♥ ♠ ♣ ♦ ♥ ♠ ♣ ♦ ♥ ♠ ♣ ♦ ♥"
cc = [23, 11.5, "表中字符"]
str3 = str(cc[1])
str4 = cc[2]
ot = str1 +"表外字符： " + str3 + str4
print(ot)
f = open("../data/output/record.txt", "a", encoding="utf8")
f.write(ot)
f.close()
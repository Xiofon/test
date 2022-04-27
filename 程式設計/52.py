s1 = "紅豆生南國，春來發幾枝。願君多采擷，此物最相思。"
s2 = "春眠不覺曉，處處聞啼鳥。夜來風雨聲，花落知多少。"
ans = []
for i in range(0,len(s1)):
    for c in range(0,len(s1)):
        if s1[i] == s2[c] and (s1[i] != "，" and s1[i] != "。"):
            ans.append(s2[c])
print(ans)
---
title: input
level: medium
flag: FLAG{Cr055_5iTE_5CRIptINg}
writer: iwat
---

# input

## 問題文

Let's execute the alert function!

## 解法

問題文からAlert関数を実行すれば良いことがわかる。<br>
開発者ツール等でコードを確認すると、innerHTMLを使用していることから、XSSの脆弱性がある事が分かる。<br>
入力欄にXSS入力することでAlertが実行されFLAGを取得することができる。<br>
```<img src=1 onerror=alert()>```






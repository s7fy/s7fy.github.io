+++
date = '2026-01-05T20:44:14+09:00'
title = 'article_script'
tags = ['2026', '2026-01']
draft = false
+++

# 記事のテンプレートを自動生成させる

hugoでは、[Front Matter](https://gohugo.io/content-management/front-matter/)と呼ばれる機能をサポートしています。  
ただ、これを書くのがめんどくさいんですよね。  
そこで、記事を書く際に情報を自動的に記入するシェルスクリプトを書きました。

```sh
#!/bin/zsh
set -e

cd ~/blog

if [ -z "$1" ]; then
  echo "usage: $0 article_name"
  exit 1
fi

POST="/your/path/content/posts/$1.md"

DATE=$(date "+%Y-%m-%dT%H:%M:%S+09:00")
TAG_Y=$(date "+%Y")
TAG_YM=$(date "+%Y-%m")

if [ -e "$POST" ]; then
  echo "already exists: $POST"
  exit 1
fi

cat <<EOF > "$POST"
+++
date = '$DATE'
title = '$1'
tags = ['$TAG_Y', '$TAG_YM']
draft = true
+++

EOF

echo "made it : $POST"

vim $POST
```
シェルスクリプトの動きを簡単に紹介します。

* 記事名を入力する
* 決められたディレクトリに記事名.mdを作成する。
* dateコマンドで現在時刻を整形して取得 → Front Matterに埋め込む
* vimコマンドを実行し、即座に記事が書き始められます。


このようにテンプレートが挿入されて、悩まずに書き始められるようになりました。

```
+++
date = '2026-01-05T20:44:14+09:00'
title = 'article_script'
tags = ['2026', '2026-01']
draft = true
+++
```

{{< callout type="warning" text="投稿するときは、下書き状態をfalseにするのを忘れないように" >}}

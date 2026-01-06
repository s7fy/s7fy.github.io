+++
date = '2026-01-06T10:46:40+09:00'
title = 'vimrc_mac'
tags = ['2026', '2026-01', 'register', 'vim', 'mac']
draft = false
+++

# Macで`yy + p`が使えない！！
Macでvimで作業するときの基礎コマンドである`ヤンク`と`ペースト`ですが、
Macでは`.vimrc`に設定をしないと`ペースト`ができないようです。
以下のように設定をしたら解決しました。

```.vimrc
set clipboard=unnamed,unnamedplus
```  
{{< callout type="warning" text="以下の設定では、システムクリップボードレジスタが使えないので機能しなかったです。" >}}

```.vimrc
set clipboard=unnamedplus
```
念の為、`unnamed`と`unnamedplus`を指定しました。
どうやら、`unnamedplus`というのはunix系のレジスタで扱うシステムクリップボードのレジスタのようです。  
なので、Macは`unnamed`を指定するとうまくいくみたいです。  
vimでの`ヤンク`とOSでの`クリップボード`では格納されるレジスタや参照されるレジスタが違うので、うまく機能しなかったのかなと思います。  
[参考にした記事:  .vimrcの設定](https://github.com/Neos21/dotfiles/blob/master/.vimrc) 

[参考にした記事: レジスタ一覧](https://qiita.com/0829/items/0b3f63798b6910623efc#9--%E6%9C%80%E7%B5%82%E6%A4%9C%E7%B4%A2%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3%E7%94%A8%E3%83%AC%E3%82%B8%E3%82%B9%E3%82%BF-)  

[参考にした記事: レジスタ一覧(英語ソース)](https://vimdoc.sourceforge.net/htmldoc/change.html#registers)  


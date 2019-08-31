# 有序列表

第一个有序列表

1. item
    1. item
    2. item
        1. item
        2. item
        3. item
    3. item
2. item
3. item

第二个有序列表

1. item
    1. item
    2. item
        1. item
        2. item
        3. item
    3. item
2. item
3. item

# 插入SVG

<!--
![Windows_Logo_SVG](https://upload.wikimedia.org/wikipedia/commons/2/2b/Windows_logo_2012-Black.svg?sanitize=true)
-->
![Win][Windows_Logo_20px]![Win][Windows_Logo_16px]![Win][Windows_Logo_12px]

[Windows_Logo_20px]: https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Windows_logo_2012-Black.svg/20px-Windows_logo_2012-Black.svg.png
[Windows_Logo_16px]: https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Windows_logo_2012-Black.svg/16px-Windows_logo_2012-Black.svg.png
[Windows_Logo_12px]: https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Windows_logo_2012-Black.svg/12px-Windows_logo_2012-Black.svg.png

# 不会被去掉的标签

Some text <span class="remark">use span do more style</span>, some <i>use i</i>, some <b>use b</b>, some <em>use em</em>, some <strong>use strong</strong>, some deed not.  
GitHub just use `<em>` for `*`, `<strong>` for `**`.  
So we can use `<span><i>...</i></span>` (like <span><i>this</i></span>) with Stylus to format some special content.
- 尝试为列表写一些注解
    - 第一项内容  
      <span><i>这里是对第一项内容的一些说明，应该也可以使用*斜体*和**粗体**的`Markdown`标记来进行格式化。  
      双空格折行应该也能支持。
      </i></span>
    - 第二项内容  
      <span><b>这里是对第二项内容的一些说明，应该也可以使用*斜体*和**粗体**的`Markdown`标记来进行格式化。  
      双空格折行应该也能支持。
      </b></span>
    - 第三项内容  

# 斜体、粗体、删除线

|语法|效果|
|----|-----|
|`*斜体1*`|*斜体1*|
|`_斜体2_`| _斜体2_|
|`**粗体1**`|**粗体1**|
|`__粗体2__`|__粗体2__|
|`这是一个 ~~删除线~~`|这是一个 ~~删除线~~|
|`***斜粗体1***`|***斜粗体1***|
|`___斜粗体2___`|___斜粗体2___|
|`***~~斜粗体删除线1~~***`|***~~斜粗体删除线1~~***|
|`~~***斜粗体删除线2***~~`|~~***斜粗体删除线2***~~|

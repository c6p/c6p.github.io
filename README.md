# Foam-mkdocs-template

![foam-mkdocs-template-png](demo-mkdocs.png)

* Share your **foam/obsidian/markdown** notes in a simple and intuitive way ! Support [[roamlike link]] 
* 用简单和直观的方式分享你的foam/obsidian/markdown笔记！支持[[链接]]解析。

This template use [mkdocs](https://www.mkdocs.org/user-guide/configuration/), [mkdocs-material](https://squidfunk.github.io/mkdocs-material/), [mkdocs-roamlinks-plugin](https://github.com/Jackiexiao/mkdocs-roamlinks-plugin) and many mkdocs plugins.


## Demo-样例

* [github page](https://jackiexiao.github.io/blog/)
* For Chinese User, visit [gitee page](https://jackiegeek.gitee.io/blog/)

## Support syntax支持的语法

| origin原始                  | convert转换后                             |
| ----------------------- | ----------------------------------- |
| `[Git Flow](git_flow.md)` | `[Git Flow](../software/git_flow.md)` |
| `[[Git Flow]]`            | `[Git Flow](../software/git_flow.md)` |
| `![[image.png]]`           | `![image.png](../image/imag.png)`      |
| `[[#Heading identifiers]]` | `[Heading identifiers in HTML](#heading-identifiers-in-html)`
| ` [[Git Flow#Heading]]` | `[Git Flow](../software/git_flow.md#heading)` |



## Usage：Deploy to github page

1. fork this repository 
2. add your documents to `docs` , `docs/index.md` is the main page of the website
3. open `mkdocs.yml`, modify `site_name` to your website name, this file is the setting of website, visit link below to get more information
* [mkdocs-material](https://squidfunk.github.io/mkdocs-material/)
* [mkdocs](https://www.mkdocs.org/user-guide/configuration/)
4. push to github, 
5. go to github setting, open github page, choose `gh-pages` branch, wait a moment, then visit `http://<your-github-username.github.io/<your-repo>`, for example:`jackiexiao.github.io/blog/`
5. Done! That's all! Have fun!

Thx to `Github Action`, it make deploy a blog so easy, all you need todo is modify and push your file

## Deploy Locally

The simplest way: Enter your local repo directory, make sure your python > 3.6
```
pip install mkdocs mkdocs-material mkdocs-roamlinks-plugin
mkdocs serve 
```
Then visit `http://127.0.0.1:8000/`


## 使用方法：部署到github page生成博客网站

1. 复制Fork或者下载这个仓库
2. 将你的文档添加到`docs`下面（原来的文件可以全部删掉），在`docs`吓添加一个`index.md`作为网站主页
3. 进入`mkdocs.yml`修改`site_name`为你的网站名称，这个文件包含了你网站的配置，具体配置教程见：
* [mkdocs-material](https://squidfunk.github.io/mkdocs-material/)
* [mkdocs](https://www.mkdocs.org/user-guide/configuration/)
4. push提交修改到github
5. 到你的github仓库-setting中设置github page，选择分支-gh-pages，等一小会，就会有网址啦，比如我的是`jackiexiao.github.io/blog/`
6. 大功告成！

之所以git push就可以自动部署网页，生成博客，是因为github action在起作用！感兴趣可以自己搜索一下。

## 本地部署

经常性的，我们需要本地部署文档，来进行频繁的修改和预览。最简单的方法是进入你的文件夹（仓库本地地址，也就是`docs`文件夹的上一级），你的python需要3.6以上
```
pip install mkdocs mkdocs-material mkdocs-roamlinks-plugin
mkdocs serve 
```
然后访问`http://127.0.0.1:8000/`就可以了

## 同步发布到Gitee page加速国内访问

步骤很简单，比如这个[博客](https://jackiegeek.gitee.io/blog/)，在Gitee的首页下新建仓库，在页面下方选择`导入已有仓库`, 填写你的github仓库地址，然后点击`服务`->`Gitee Page`->`部署分支`->选择`gh-pages`，点击`更新`就完成啦！几秒后刷新你就可以看到自己gitee apge的链接了。不过要注意的是，每次更新Gitee page，你需要3个步骤

1. 更新你的github仓库
2. 在Gitee中手动点击同步github
3. 按前面的步骤，再次部署Gitee Page 


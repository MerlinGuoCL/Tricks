# 批量翻译文献
## 实现技术思路
step 1 从web of science（wos）网站批量导出文献的元数据（题目、摘要、doi），导出的格式选择Excel；  
step 2 用python循环读取元数据，组装成矩阵，待处理；  
step 3 借助kimi大模型api，让它翻译题目、摘要（也可以问它其他相同问题）；  
step 4 将回答结果借助docx包写入word中，输出word；并存入待处理矩阵，输出csv。  
## 常见问题
- 包安装
    - pandas需另安装xlrd包
- kimi
    - 如果kimi未充值，每分钟和每天发起的请求数和交互token限制较大，在程序运行时会遇到不规律报错，建议加入程序休眠代码；  
    - kimi的API获取，网址：https://platform.moonshot.cn/console/api-keys；  
    - 新建的kimi账户好像有15元的赠额。
- word输出
    - 需要在程序文件夹新建一个Doc1.docx的word文件，并打开文件输入一个回车保存后退出。  
    （这是docx包的原因，新建不打开word，word未初始化，运行程序会报错）


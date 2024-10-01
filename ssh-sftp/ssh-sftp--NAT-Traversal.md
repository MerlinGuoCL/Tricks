# Ubuntu服务器ssh-sftp配置
## 安装配置ssh-sftp
```
https://blog.csdn.net/yanzhenjie1003/article/details/70184221
```
## 内网穿透
本教程的内网穿透借助的是Sakura frpc公司的服务器进行内网穿透；  
其他公司的内网穿透工具参考其他工具的使用说明；  
若同学自己有具备公网ip的服务器也可直接配置内网穿透。
```
初次配置：
安装frpc：https://doc.natfrp.com/frpc/usage.html
配置frpc后台运行和开机自启动：https://doc.natfrp.com/frpc/service/systemd.html

重启后：
step1:检查ssh是否在线
step2:直接用frpc命令链接隧道
```

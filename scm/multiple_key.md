## 语言

```shell
git config --global core.quotepath false 
git config --global gui.encoding utf-8
git config --global i18n.commit.encoding utf-8 
git config --global i18n.logoutputencoding utf-8 
set LESSCHARSET=utf-8
```



## 取消全局设置

```shell

git config --global --unset user.name
git config --global --unset user.email

# project folder
git config user.email  vicky_yang@iepds.com
git config user.name vicky
```




## key
### 1 生成Key

```shell
ssh-keygen -t rsa -C vicky_yang@iepds.com
ssh-keygen -t rsa -C yaya_vicky@hotmail.com
ssh-keygen -t rsa -C rhyme_yang@live.cn


```

### 2 创建 config

.ssh 目录下

```shell
#Default github 
Host github.com  
HostName github.com
PreferredAuthentications publickey
IdentityFile C:\Users\vicky\.ssh\id_rsa_epds

#second user
Host yaya
HostName github.com
PreferredAuthentications publickey
IdentityFile C:\Users\vicky\.ssh\id_rsa_yaya_vicky

#third user
Host rhymehub
HostName github.com
PreferredAuthentications publickey
IdentityFile C:\Users\vicky\.ssh\id_rsa_rhyme
```
### 3 测试

```shell
ssh -T git@yaya
```

### 4. 使用新的公私钥

```shell
# org path
git clone git@github.com:yayavicky/notes.git

# actual use
git clone git@yaya:yayavicky/notes.git
git git@yaya:yayavicky/EpdsTestPlatform.git
```

## tag

```shell
git tag -l

git push origin --tags
git push origin tagname

git branch -d gu
git push origin --delete gu
```


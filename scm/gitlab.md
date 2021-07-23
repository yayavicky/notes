https://about.gitlab.com/install/#ubuntu



## ubuntu 环境

```shell
dpkg -l | grep ssh
sudo apt-get install openssh-server
dpkg -l | grep ssh
ps -e | grep ssh

sudo /etc/init.d/ssh start
sudo service ssh start 

systemctl status sshd
systemctl start sshd
sudo systemctl enable ssh

sudo /etc/init.d/ssh stop 
sudo /etc/init.d/ssh start

ssh username@192.168.1.103 

hostname
epds-PowerEdge-T20
```

## Add user

```shell
sudo adduser vicky
usermod -aG sudo vicky

cat /etc/sudoers.d/vicky

vicky ALL=(ALL) NOPASSWD: ALL
```



## install gitlab

```shell
sudo apt-get update
sudo apt-get install -y curl openssh-server ca-certificates tzdata perl

sudo apt-get install -y postfix

#curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/script.deb.sh | sudo bash

curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.deb.sh | sudo bash

sudo apt-get install gitlab-ce=14.0.1-ce.0
```

Please configure a URL for your GitLab instance by setting `external_url`
configuration in /etc/gitlab/gitlab.rb file.



Then, you can start your GitLab instance by running the following command:
  sudo gitlab-ctl reconfigure

192.168.2.167

+ [gitlab-ce_14.0.1-ce.0_arm64.deb](https://packages.gitlab.com/gitlab/gitlab-ce/packages/ubuntu/focal/gitlab-ce_14.0.1-ce.0_arm64.deb)
+ [install doc](https://docs.gitlab.com/omnibus/installation/)



root 2Wsx3edc



+ [GitLab基础：增量式备份的实现方式](https://blog.csdn.net/liumiaocn/article/details/107936967)
+ [GitLab基础：备份与恢复指南](https://liumiaocn.blog.csdn.net/article/details/107952592)



+ 添加用户
  + http://192.168.2.167/admin/users



[gitlab新建项目过程和添加用户](https://blog.csdn.net/weiqiang0124/article/details/80803280)


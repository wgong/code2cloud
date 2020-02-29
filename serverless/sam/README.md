aws cloudformation package (sam package)
aws cloudformation deploy (sam deploy)

https://aws.amazon.com/serverless/sam/
https://github.com/awslabs/aws-sam-cli

install docker on ubuntu
https://docs.docker.com/install/linux/docker-ce/ubuntu/

$ sudo apt-get remove docker docker-engine docker.io containerd runc

$ sudo apt-get update

$ sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common

$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

$ sudo apt-key fingerprint 0EBFCD88

$ sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

$ sudo apt-get update

$ sudo apt-get install docker-ce docker-ce-cli containerd.io


$ apt-cache madison docker-ce
 docker-ce | 5:19.03.6~3-0~ubuntu-eoan | https://download.docker.com/linux/ubuntu eoan/stable amd64 Packages

$ export VERSION_STRING=5:19.03.6~3-0~ubuntu-eoan
$ sudo apt-get install docker-ce=$VERSION_STRING docker-ce-cli=$VERSION_STRING containerd.io

$ sudo service docker status
$ sudo service docker start

#enable docker to start on boot
$ sudo systemctl enable docker

#check status=enabled
$ sudo systemctl status docker


$ sudo docker run hello-world

How to let unprivileged user run docker
https://docs.docker.com/install/linux/linux-postinstall/

#install homebrew - https://docs.brew.sh/Homebrew-on-Linux
sh -c "$(curl -fsSL https://raw.githubusercontent.com/Linuxbrew/install/master/install.sh)"

- Install the Homebrew dependencies if you have sudo access:
  Debian, Ubuntu, etc.
    sudo apt-get install build-essential
  Fedora, Red Hat, CentOS, etc.
    sudo yum groupinstall 'Development Tools'
  See https://docs.brew.sh/linux for more information.
- Configure Homebrew in your ~/.profile by running
    echo 'eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv)' >>~/.profile
- Add Homebrew to your PATH
    eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv)
- We recommend that you install GCC by running:
    brew install gcc
- Run `brew help` to get started
- Further documentation: 
    https://docs.brew.sh

$ sudo apt install linuxbrew-wrapper

$ brew --version
Homebrew 2.2.6
Homebrew/linuxbrew-core (git revision 946527; last commit 2020-02-28)

#install AWS SAM CLI
$ brew tap aws/tap
$ brew install aws-sam-cli

#################################################################333
A CA file has been bootstrapped using certificates from the system
keychain. To add additional certificates, place .pem files in
  /home/linuxbrew/.linuxbrew/etc/openssl@1.1/certs

and run
  /home/linuxbrew/.linuxbrew/opt/openssl@1.1/bin/c_rehash

openssl@1.1 is keg-only, which means it was not symlinked into /home/linuxbrew/.linuxbrew,
because this is an alternate version of another formula.

If you need to have openssl@1.1 first in your PATH run:
  echo 'export PATH="/home/linuxbrew/.linuxbrew/opt/openssl@1.1/bin:$PATH"' >> ~/.bash_profile

For compilers to find openssl@1.1 you may need to set:
  export LDFLAGS="-L/home/linuxbrew/.linuxbrew/opt/openssl@1.1/lib"
  export CPPFLAGS="-I/home/linuxbrew/.linuxbrew/opt/openssl@1.1/include"

For pkg-config to find openssl@1.1 you may need to set:
  export PKG_CONFIG_PATH="/home/linuxbrew/.linuxbrew/opt/openssl@1.1/lib/pkgconfig"

==> python
Python has been installed as
  /home/linuxbrew/.linuxbrew/bin/python3

Unversioned symlinks `python`, `python-config`, `pip` etc. pointing to
`python3`, `python3-config`, `pip3` etc., respectively, have been installed into
  /home/linuxbrew/.linuxbrew/opt/python/libexec/bin

You can install Python packages with
  pip3 install <package>
They will install into the site-package directory
  /home/linuxbrew/.linuxbrew/lib/python3.7/site-packages

See: https://docs.brew.sh/Homebrew-and-Python
###################################################

$ /home/linuxbrew/.linuxbrew/bin/sam --version
SAM CLI, version 0.43.0

#add linuxbrew - package manager due to AWS SAM CLI dependency
#~/.bashrc
export PATH="$PATH:/home/linuxbrew/.linuxbrew/bin"


#next step for SAM
Hello SAM
- https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-hello-world.html

AWS SAM example apps
- https://github.com/aws-samples/serverless-app-examples

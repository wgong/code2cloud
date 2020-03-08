AWS CDK - Cloud Dev Kit
use imperative lang such as python to author IaC - Infrastructure as Code, 
CloudFormation is a declarative way to describe cloud resources/stack, but it is low-level,
CDK is a higher-level abstraction to describe infrastructure more simply.

Getting Started With the AWS CDK
- https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html
- [CDK examples in python](https://github.com/aws-samples/aws-cdk-examples#Python)

Python CDK examples 
- https://github.com/aws-samples/aws-cdk-examples/tree/master/python

CDK Workshop
- https://cdkworkshop.com/

Getting started with the AWS Cloud Development Kit and Python 
- https://aws.amazon.com/blogs/developer/getting-started-with-the-aws-cloud-development-kit-and-python/

#upgrade npm
$ sudo npm cache clean -f
$ sudo npm install -g n
$ sudo n stable
$ npm --version
6.13.4
$ node --version
v12.16.1

#install
$ sudo npm install -g aws-cdk
$ which cdk
/usr/local/bin/cdk

$ cdk --version
1.26.0 (build e251651)

$ pip install --upgrade aws-cdk.core


You can use the env property on a stack to specify the account and region used when deploying a stack
MyStack(app, "MyStack", env=core.Environment(region="REGION",account="ACCOUNT")

#hello-cdk
$ mkdir hello-cdk
$ cd hello-cdk

$ cdk init --language python
Applying project template app for python
Executing Creating virtualenv...

# Welcome to your CDK Python project!

This is a blank project for Python development with CDK.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the .env
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .env
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .env/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .env\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!


$ cdk deploy
HelloCdkStack: deploying...
HelloCdkStack: creating CloudFormation changeset...
 0/3 | 10:28:20 PM | CREATE_IN_PROGRESS   | AWS::S3::Bucket    | MyFirstBucket (MyFirstBucketB8884501) Resource creation Initiated
 0/3 | 10:28:21 PM | CREATE_IN_PROGRESS   | AWS::CDK::Metadata | CDKMetadata Resource creation Initiated
 1/3 | 10:28:21 PM | CREATE_COMPLETE      | AWS::CDK::Metadata | CDKMetadata 
 2/3 | 10:28:41 PM | CREATE_COMPLETE      | AWS::S3::Bucket    | MyFirstBucket (MyFirstBucketB8884501) 
 3/3 | 10:28:43 PM | CREATE_COMPLETE      | AWS::CloudFormation::Stack | HelloCdkStack 

 ✅  HelloCdkStack

Stack ARN:
arn:aws:cloudformation:us-east-1:57824746:stack/HelloCdkStack/81f752e0-5aa3-11ea-ae89-0a0faac5843d



######################################################################

https://aws.amazon.com/blogs/developer/getting-started-with-the-aws-cloud-development-kit-and-python/

$ cd ~/projects/code2cloud/cdk
$ mkdir my_python_sample
$ cd my_python_sample
$ cdk init --language python sample-app
$ source .env/bin/activate
$ pip install -r requirements.txt
$ cdk synth
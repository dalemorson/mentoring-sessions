# Bash and AWS CLI

In this session we'll learn how to create a few Bash scripts containing AWS CLI commands in order to provision S3 buckets.

## What is the AWS CLI?

The AWS Command Line Interface (AWS CLI) is an open source tool that enables you to interact with AWS services using commands in your command-line shell. With minimal configuration, the AWS CLI enables you to start running commands that implement functionality equivalent to that provided by the browser-based AWS Management Console from the command prompt in your terminal program.

## Pre-reqs

1. You'll need a Cloudreach provided account via the [AWS Vending Machine](https://aws.vending-machine.cloudreach.io/home/welcome). Full instructions available on [Confluence](https://cloudreach.jira.com/wiki/spaces/IT/pages/3704979661/New+AWS+Labs), OR your own AWS lab.
2. [Create an IAM user account and an access key ID / secret access key pair.](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-prereqs.html)
3. [Install the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
4. [Follow the configuration basics](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)

Now let's jump straight into some tasks!

## Task 10

Create three S3 buckets via the AWS Management Console:
- What are the potential disadvantages or risks of creating multiple instances of an AWS service manually in the Management Console?

## Task 11

Create three S3 buckets via the AWS CLI:
- Can you find the AWS CLI command you need to use?
- What are the disadvantages or risks of using this method? 
- What AWS CLI command do you use to list your buckets?

## Task 12

Create a Bash script to automate the creation of ten S3 buckets with the following requirements:
- Use a `for` loop statement with the same prefix for the bucket name i.e. `mentoring-bucket-prefix-1`, `mentoring-bucket-prefix-2` and so on...
- What were the advantages of this method of creating buckets?

## Task 13

Create a Bash script to automate the creation of one or more buckets with the following requirements:
- Use a `for` loop statement.
- Use `arguments` to pass in individual names of buckets you want to create.
- Loop through each of the arguments passed in and create buckets with those arguments.
- Hint: use `$@` to get all arguments within the `for` loop.

## Question

How could you expand on these scripts? 

## Resources

- Search GitHub for useful [AWS CLI Bash](https://github.com/search?q=aws+cli+bash+scripts) scripts.
- [AWS CLI](https://docs.aws.amazon.com/cli/index.html)
- [AWS CLI Command Reference](https://awscli.amazonaws.com/v2/documentation/api/latest/index.html)


## Clean-up - Delete all buckets

Only delete all buckets if you created them for this session!

```
for bucket in $(aws s3 ls | awk '{print $3}'); do  aws s3 rb "s3://${bucket}" --force ; done
```

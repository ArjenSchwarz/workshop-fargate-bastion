# Step 3

Add all the required permissions to your Lambda function and make it create a securitygroup linked to your name.

Please note that if you use the SAM function, you will always need to package and deploy the template after you make changes. And if you add parameters, such as your VPC, you will need to supply these. For example:

```bash
aws cloudformation package --template-file bastion-lambda.yml --s3-bucket "doesnotexist.ig.nore.me" --output-template-file packaged-bastion.yml
aws cloudformation deploy --template-file packaged-bastion.yml --stack-name bastion-functions --capabilities CAPABILITY_IAM --parameter-overrides BastionVpc=vpc-12345678
```



## Lambda permissions

It's time to extend our SAM template, by ensuring the Lambda function can do everything it needs to do. It requires the following permissions:

* The ability to create a securitygroup and attach an ingress rule to it
* The ability to describe a network interface
* The ability to run a task on your ECS cluster
* The ability to pass a role to your task

Each of these requirements can be finegrained, and will likely require related abilities. For example, you will need the ability to see task definitions when you create them.

## Accept your name as a parameter and collect IP

The Lambda function should be able to accept your name as a parameter and parse the IP address you're accessing it from into a CIDR format (basically add /32). For example use a request parameter called **user**, so that if you call it with a slightly modified curl command it will return that.

```bash
curl -X POST https://yourapiidentifier.execute-api.us-east-1.amazonaws.com/Prod?user=arjen
# Result: "Hello arjen from 127.0.0.1/32"
```

## Create the security group

Update your Lambda function to create a securitygroup that is only opened on port 22 to the IP you invoke the Lambda function from. No other ports should be opened either. Make sure the securitygroup is named `bastion-$YOURNAME`. For creating a securitygroup you require a VPC ID, so make sure that you provide this as an environment variable and as a parameter to your SAM template. For this workshop it is easiest to use the default VPC, but if you prefer to use a different one that is possible, just make sure that it has at least one public subnet.

Please note that you can't create multiple securitygroups with the same name so if you create it, you will need to delete it before you can create it again. While testing this part, it might be easier to use different names. The example code does not take into account the situation where a securitygroup already exist, that is out of scope. Although the bonus step of the workshop will delete it when you tear down the stack.

## Testing

After running the same curl command as earlier, you should be able to see a securitygroup in your VPC that has your name and your IP address as the only ingress point.
# Step 4

Run the Fargate task when calling the Lambda function

## Add the subnets to the template and Lambda function

When running a Fargate task, you will need to provide the subnets it runs in. Add this as a parameter to the SAM template and as an environment variable to the Lambda function.

For obvious reasons, you will need to provide public subnets as the parameters.

## Make the Lambda function invoke the ECS run command for your Fargate container

Update the Lambda function to run a Fargate task that uses the task definition you defined in step 1 (bastion-$YOURNAME) and has a public IP assigned to it.

## Test

Verify that calling the Lambda function with the curl command has indeed spun up the container, check what the public IP is and then ssh into it with `ssh -i $PATH_TO_YOUR_PRIVATE_KEY root@$IP`.
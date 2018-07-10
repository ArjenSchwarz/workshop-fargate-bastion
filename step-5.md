# Step 5 / Bonus step

Usability improvements. A couple of improvements you can make to what you have. It is not limited to this, and I urge you to look at the [main repository for this project](https://github.com/ArjenSchwarz/fargate-bastion) to see more.

## Make the Lambda function return the IP address of the Bastion container

Write something that ensure the Lambda function returns the IP address of the Bastion container. Keep in mind that there is a delay between triggering the run command for the Fargate container and the ENI for it being available.

## Make the Lambda function check if the Bastion is already running, and if so, return its IP immediately

If you invoke the Lambda function a second time, it should return an existing bastion instead of trying to create a new one.

## Add some error management

Things can go wrong, clean that up.

## Make it possible to remove the bastion host

This can be either on demand, or on a schedule.
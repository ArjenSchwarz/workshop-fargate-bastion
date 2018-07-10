# Step 1

Goal: Create an ECS cluster, an ECR repository and upload your own personalised SSH Docker image in there.

## ECS Cluster

Ensure you have an ECS cluster to use with Fargate. If AWS created a "default" cluster in your account, you can use this. Otherwise, create one manually or by using the `ecs-cluster.yml` CloudFormation template present in step 2.

Please be aware that at this time Fargate is not available in all regions. If your preferred region does not yet support it, I recommend you use us-east-1 for now.

## ECR Repo

Create an ECR Repo that you wish to store your Docker container in. When you create this you will see the authentication steps you need to be able to upload an image.

## Create Docker image

Use the provided `Dockerfile` in the `docker` directory to build an image and upload it to ECR. If you look at the Dockerfile, you will see that it requires you to have a public key present in that directory. After copying your public SSH key to the docker directory you can run the below commands to build and push the image (replacing placeholders).

```bash
docker build -t $REPONAME:$YOURNAME .
docker tag $REPONAME:$YOURNAME $ACCOUNTNUMBER.dkr.ecr.$REGION.amazonaws.com/$REPONAME:$YOURNAME
docker push $ACCOUNTNUMBER.dkr.ecr.$REGION.amazonaws.com/$REPONAME:$YOURNAME

# Example
# docker build -t bastion:arjen .
# docker tag bastion:arjen 1234567890:dkr.us-east-1.amazonaws.com/bastion:arjen
# docker push 1234567890:dkr.us-east-1.amazonaws.com/bastion:arjen
```

## Create a task definiton

Create a task definiton for your image. Make sure this is a Fargate compatible definition, using the minimum allowed specs and uses your pushed up image as the only container definition.
# Step 2

Create a Lambda function and API Gateway with a placeholder codebase. The workshop uses a [SAM template](https://github.com/awslabs/serverless-application-model) to build this, but as always you can do it in a different way. Using a SAM template is likely the easiest way to do it though as it allows you to combine the Lambda function and its API Gateway to work together.

## Lambda function

Create a Lambda function using your own preferred Lambda supported language (the workshop uses Python, but you can use whatever you prefer), called **CreateBastion** and have it return a simple string of "Hello Serverless Bastion!"

## API Gateway

Create an API Gateway that is connected to this Lambda function on the root endpoint (/) with **POST** as the method.

## SAM Template Deployment

If you want to use a SAM template, you will require an additional S3 bucket in your environment that you can use for the storage of your application code when you package the file. Assuming you named your template `bastion-lambda.yml`, packaging your SAM template uses the following command (where you replace the S3 bucket name with your own):

```bash
aws cloudformation package --template-file bastion-lambda.yml --s3-bucket "doesnotexist.ig.nore.me" --output-template-file packaged-bastion.yml
```

This will upload the zipped version of your Lambda code to that bucket and generate a template file called `packaged-bastion.yml`. This is a file you should never directly edit, and only serves as a deployment tool. When you make changes, make sure you make them to your template file.

Once you have the packaged file you can then easily deploy it, both the first time and subsequent updates, with the following command:

```bash
aws cloudformation update-stack --template-file packaged-bastion.yml --stack-name bastion-functions --capabilities CAPABILITY_IAM
```

The IAM capabalities flag is required for a serverless application.

## Testing

Check what your endpoint is, and make sure that you pick the one that includes the Prod stage. Then make a curl call (or your chosen API interaction tool) to your endpoint to check that it does indeed return a successful message:

```bash
curl -X POST https://yourapiidentifier.execute-api.us-east-1.amazonaws.com/Prod/
```
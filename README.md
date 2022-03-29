sam build && sam deploy --s3-bucket cf-s3-source
sam init
sam build

sam local invoke

## Deploy
- deploy with guide.
`sam deploy –guided`
- deploy with env.
`sam deploy --config-env development`


## Delete stack, destroy resources
`aws cloudformation delete-stack --stack-name sam-app --region us-east-2`
`sam delete --stack-name TEXT --region TEXT`

## Sync stask, purpose for development (in beta, sometime bug)
`sam sync --stack-name sam-app --watch`



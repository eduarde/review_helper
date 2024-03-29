# reviews_helper

Prerequisites:

1. Install python locally (ex: 3.7.3).
2. Create a Lambda function on AWS.
   Choose python 3.7 as Runtime and choose 'app.lambda_function.lambda_handler' as handler.
   Remember the name of your lambda, it will used in step 7.

3. Create a variables.py file. Take variables_example.py as example. 


Steps:

1. Install a virtualenv lib via:
```
 pip install virtualenv
```

2. Navigate to the root of this project.
3. Create a virtualenv (venv) via command:
```
virtualenv venv
```
4. Activate the virtualenv: 

linux:
```
source venv/bin/activate
```

win:
```
venv/Scripts/activate
```

5. Install requirements.
```
pip install -r requirments.txt
```

6. Prepare the deployment package for aws.
Readme: https://docs.aws.amazon.com/lambda/latest/dg/python-package.html

In aws documentation they specify that you have to deactivate the venv.
```
deactivate
```

```
cd venv/lib/python3.7/site-packages
zip -r ../../../../my-deployment-package.zip .
```

7. Deploy and Update. (whenever you update the code). Navigate to the root of the project and run the following commands:
```
zip -g my-deployment-package.zip app/__init__.py app/lambda_function.py app/variables.py
aws lambda update-function-code --function-name generate_review --zip-file fileb://my-deployment-package.zip
```

# super_dan
Don't go to that street today. For now predicting larcenies vs burglaries

For development:
```
git clone https://github.com/Italosayan/super-dan.git
export PYTHONPATH="/Users/path/to/super_dan":$PYTHONPATH # Add pythonpath to what it already is
cd super-dan
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

-Change "/Users/path/to/super_dan" to path where the project was cloned

Each part of the pipeline is independent:

* Getting the data
* Data preprocess
* Training

```
python3 super_dan_app/dataset/get_data.py
python3 super_dan_app/dataset/pre_processing.py
python3 training/training.py
```

For testing:

```
python -m pytest
```

Great Expectations workflow and basics

* Suite: Group of expectations
* Expectation : Data test

```
great_expectations suite list
great_expectations init # Only ran once
great_expectations docs build # See expectations in jupyter
great_expectations suite edit # Edits a data doc
great_expectations suite new # Create new group of tests.(Use when new sql or new data source)
```

* Workflow
```
great_expectations tap new day_2020-04-04_crimes day_2020-04-04_crimes_test.py
```

Execute Jenkins
```
export JAVA_HOME=$(/usr/libexec/java_home -v 1.8)
java -jar jenkins.war --httpPort=8080

brew cask install homebrew/cask-versions/adoptopenjdk8
brew install jenkins-lts
brew services start jenkins-lts
Go to localhost
https://stackoverflow.com/questions/43987005/jenkins-does-not-recognize-command-sh/48634476
https://stackoverflow.com/questions/54452082/jenkins-docker-command-not-found-path-setup
https://stackoverflow.com/questions/50333325/jenkins-cannot-run-program-docker-error-2-no-such-file-or-directory
https://www.edureka.co/community/8365/permission-denied-error-while-running-simple-job-in-jenkins
Remember to not have empty env variables in jenkins

dockers and jenkins video
https://www.youtube.com/watch?v=ppCzDDpcqRk&feature=youtu.be
```

Workflow
```
After a commit execute jenkins:
Docker, great_expectations and pytest will be executed
```

Next Steps:

1. [x] Set up test workflow: Always run the full test suite before a coding session, and run it again after. This will give you more confidence that you did not break anything in the rest of the code.
2. [x] Set up Jenkins job
3. [x] Set up WandB with current model.
4. [x] Think about workflow and best practices
5. [x] Deploy Pipeline that outputs .pkl to the API using Metaflow
6. [x] Deploy the API using Sagemaker.
7. [ ] Load test (extra)
8. [ ] Endpoint monitoring in sagemaker
9. [x] Setup experimentation job in jenkins. (wndb metrics)
10. [x] Multi branch experimentation job in jenkins. (wndb metrics)
12. [ ] Setup deployment job in jenkins.
13. [ ] Define how the experimentation and deployment job related.
14. [ ] Setup data exploration/concept drift job in jenkins. (expectations)
15. [ ] Read sequoia stuff. 
16. [X] Read Ml in prod
17. [X] Read aws managing data science

Workflow Advice
* Test to know if code works
* Remove fear
* When code is changed add a test
* When a bug is found write a test
* Test explains how
* Write comments to explain why

Experimentation:
* Weights and biases is a great way to store runs
* Experimentation iteration?
* One candidate model per branch. The experimentation job in jenkins has branch as a input
* One experimentation job can be in aws the other local.
* Production is in master. Deployment trains and deploys to aws

Production:
* Metaflow
* Sagemaker
    
5. Deployment
    * AWS Sagemaker
        0. export AWS_PROFILE=italouser
        0. aws configure --profile italouser
        1. build_and_push.sh name-of-estimator: Image pushed to ecr
        2. ARN_USER is defined in .zprofile
        3. Change name-of-estimator in sage_sdk_setup_train.py
        4. run sage_sdk_setup_train.py (without deploy command)
            - uploads training data
            - Writes model artifacts to s3 inside output sub directory
            - sagemaker-eu-west-1/output/decision-tree/output model artifact
        5. run sage_sdk_setup_train.py (with deploy command)
            - the deploy command: 
            - Upload train/serve image to sagemaker with a image type and count.
            - Endpoint config and creation
            - Model in sagemaker
        6. Change endpoint name and run sage_sdk_get_requests.py
            
        
    ML in production: 
    WSGI: server and application communication 
    Http -> Nginx(Distributes to workers) -> HTTP -> Gunicorn workers parse http using wsgi and pass inputs to python application -> (flask or django or anything)
    1. Nginx is a light-weight layer that handles the incoming HTTP requests and manages the I/O in and out of the container efficiently.
    2. Gunicorn is a WSGI pre-forking worker server that runs multiple copies of your application and load balances between them.
    3. Flask is a simple web framework used in the inference app that you write. It lets you respond to call on the /ping and /invocations endpoints without having to write much code.
    
    Which aws instance should I use and how many?
    What will be the load?
    
    https://stackoverflow.com/questions/15979428/what-is-the-appropriate-number-of-gunicorn-workers-for-each-amazon-instance-type
    https://github.com/garnaat/missingcloud
    
    Sagemaker deploy explanation:
    1. Training job(docker-tag train) 
        1. Input training data to the sagemaker session using upload_data.
        2. AWS executes your train code. Gets data and trains.
        3. Train code writes model output to opt/ml/model and sagemaker copies it to s3.
    2. Deploy(docker-tag serve):  
        1. Creates deployable model: Gets it from s3. The location specified in the output_path of ESTIMATOR.
        2. Configures endpoint
        3. Launches the endpoint

6. Monitoring
    * Datadog
    * Computer performance monitoring

Articles:
* https://medium.com/sequoia-capital/sequoia-data-science-8a76098035a4
* https://www.fast.ai/2020/01/07/data-questionnaire/
* https://d1.awsstatic.com/whitepapers/aws-managing-ml-projects.pdf
* http://martin.zinkevich.org/rules_of_ml/rules_of_ml.pdf
* https://www.oreilly.com/radar/drivetrain-approach-data-products/

Tools to explore:
* https://pycaret.org/
* Summarize wandb plots
* https://pair-code.github.io/what-if-tool/
* https://flyte.org/
* https://www.kaggle.com/learn/machine-learning-explainability
* https://christophm.github.io/interpretable-ml-book/

Workflow 2.0



contact : superdancontact@gmail.com

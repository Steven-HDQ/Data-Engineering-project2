
pipeline{
  agent any
  
  stages {
    stage('Build'){
      steps{
       echo 'Building App'
       sh 'docker build -t myapp2'
        }
      }
    stage('Run'){
      steps{
       echo 'running'
       sh 'docker-compose up'
        }
      }
    stage('Test'){
      steps{
       echo 'Testing'
       python test_app.py
        }
      }
    stage('Finish'){
      steps{
       echo 'Success'
        }
      }
    }
}
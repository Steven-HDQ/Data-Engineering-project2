
pipeline{
  agent any
  
  stages {
    stage('Build'){
      steps{
       echo 'Building App'
       bat 'docker build -t myapp2 .'
        }
      }
    stage('Run'){
      steps{
       echo 'Running'
       bat 'docker run -d -p 5000:5000 --name myapp2_c myapp2'
        }
      }
    stage('Test'){
      steps{
       echo 'Testing'
       bat 'python test_app.py'
        }
      }
    stage('Remove'){
      steps{
       echo 'Remove'
       bat 'docker stop myapp2_c'
       bat 'docker rmi -f myapp2'
        }
      }
    stage('Finish'){
      steps{
       echo 'Success'
        }
      }
    }
}
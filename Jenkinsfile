
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
       bat 'docker run -d -p 6379:6379 --name myredis redis:alpine'
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
       echo 'Removing'
       bat 'docker stop myapp2_c'
       bat 'docker rm myapp2_c'
       bat 'docker rmi -f myapp2'
       bat 'docker stop myredis'
       bat 'docker rm myredis'
        }
      }
    stage('Finish'){
      steps{
       echo 'Success!'
        }
      }
    }
}
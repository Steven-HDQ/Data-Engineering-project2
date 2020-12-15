
pipeline{
  agent any
  
  stages {
    stage('Build'){
      steps{
       echo 'Building App'
       bat 'docker-compose up'
        }
      }
    stage('Down'){
      steps{
       echo 'Down'
       bat 'docker-compose up'
        }
      }
    stage('Finish'){
      steps{
       echo 'Success'
        }
      }
    }
}
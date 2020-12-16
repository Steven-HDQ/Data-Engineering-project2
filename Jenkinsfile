def groovyfile
pipeline{
  agent any
  
  stages {
    
	  stage ('Build Script'){
	  	steps{
			script{
				 def filename = 'jenkins.' + env.BRANCH_NAME + '.groovy'
				 groovyfile = load filename
			}
		}
	  }
    
    stage('Build App'){
      steps{
        script{
          groovyfile.build_app()
        }
      }
    }
    stage('Testing'){
      steps{
        script{
          groovyfile.test_app()
        }
      }
    }
    stage('Docker images down'){
      steps{
        script{
          groovyfile.down_app()
        }
      }
	}
      stage(' Merge to main'){
        steps{
		script{
          groovyfile.live_app()
		}
        }
      }
    }
}
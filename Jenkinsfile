pipeline {
  agent any
  stages {
		stage('Test') {
            agent {
                docker {
                    image 'qnib/pytest'
                }
            }
            steps {
                sh 'py.test --verbose --junit-xml test-reports/results.xml test_todo.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
  }
}

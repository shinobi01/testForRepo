pipeline {
  agent {
    node {
      label 'master'
    }

  }
  stages {
    stage('1') {
      steps {
        node(label: 'Win_Bat') {
          bat(script: 'ipconfig', returnStdout: true)
        }

      }
    }

    stage('2') {
      steps {
        sleep 10
      }
    }

    stage('3') {
      steps {
        echo 'Done'
      }
    }

  }
}
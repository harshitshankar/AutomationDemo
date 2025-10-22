pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/harshitshankar/AutomationDemo.git'
            }
        }

        stage('Build Docker') {
            steps {
                sh 'docker build -t automation-demo .'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker run --rm automation-demo'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/allure-results/**', fingerprint: true
        }
    }
}

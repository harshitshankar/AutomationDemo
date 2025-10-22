pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/harshitshankar/AutomationDemo.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                // Use bat instead of sh for Windows
                bat '''
                python --version
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                pytest tests/ --alluredir=reports/allure-results
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/allure-results/**', fingerprint: true
        }
    }
}

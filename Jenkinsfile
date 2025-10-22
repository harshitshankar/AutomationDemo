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
                bat '''
                    echo Setting up Python environment...
                    python --version
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    echo Running Pytest automation tests...
                    pytest tests/ --alluredir=reports/allure-results --html=reports/report.html --self-contained-html
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                bat '''
                    echo Generating Allure report...
                    if exist reports\\allure-results (
                        echo "Allure results found, generating report..."
                    ) else (
                        echo "No allure results found!"
                    )
                '''
            }
        }
    }

    post {
        success {
            archiveArtifacts artifacts: 'reports/**/*.*', fingerprint: true
            echo "✅ Tests executed successfully. Artifacts archived."
        }
        failure {
            echo "❌ Tests failed. Check logs for details."
        }
    }
}

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
                sh '''
                    echo "Setting up Python environment..."
                    python3 --version
                    python3 -m pip install --upgrade pip
                    pip3 install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    echo "Running Pytest automation tests..."
                    pytest tests/ --alluredir=reports/allure-results --html=reports/report.html --self-contained-html
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                sh '''
                    echo "Generating Allure report..."
                    if [ -d "reports/allure-results" ]; then
                        allure generate reports/allure-results -o reports/allure-report --clean
                        echo "Allure report generated at reports/allure-report"
                    else
                        echo "No allure results found!"
                    fi
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

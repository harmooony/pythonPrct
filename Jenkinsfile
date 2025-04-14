pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'python --version'
                sh 'pip install --upgrade pip'
            }
        }
        stage('Test') {
            steps {
                sh 'python -m unittest discover -s . -p "test_*.py"'
            }
        }
        stage('Build Calculator') {
            steps {
                sh 'python calculator_pr.py'
            }
        }
    }
    post {
        always {
            junit 'report.xml'
        }
    }
}

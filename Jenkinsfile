pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Получаем код из репозитория
                git 'https://github.com/your-repository/calculator.git'
            }
        }

        stage('Set up Python') {
            steps {
                // Устанавливаем Python (предполагается, что он уже есть на агенте)
                sh 'python --version'
                sh 'pip --version'
            }
        }

        stage('Install dependencies') {
            steps {
                // Устанавливаем необходимые зависимости
                sh 'pip install tkinter'
            }
        }

        stage('Run Unit Tests') {
            steps {
                // Запускаем unit-тесты
                sh 'python -m unittest calculator_pr_test.py'
            }
            post {
                always {
                    // Сохраняем отчеты о тестах (если используются)
                    junit '**/test-reports/*.xml'
                }
            }
        }

        stage('Run Application Test') {
            steps {
                // Проверяем, что приложение запускается
                script {
                    try {
                        sh 'python calculator_pr.py & sleep 5'
                        sh 'pkill -f calculator_pr.py'
                    } catch (Exception e) {
                        error "Application test failed: ${e}"
                    }
                }
            }
        }
    }

    post {
        always {
            // Очистка после выполнения
            echo 'Pipeline completed - cleanup'
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}

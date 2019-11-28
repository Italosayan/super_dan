pipeline {
    agent { dockerfile true }
    stages {
        stage('test') {
            steps {
                sh 'python --version'
                sh 'python -m pytest'
            }
        }
        stage('build') {
            steps {
                sh 'python3 super_dan_app/dataset/get_data.py'
                sh 'python3 super_dan_app/dataset/pre_processing.py'
                sh 'python3 training/training.py'
            }
        }
    }
}
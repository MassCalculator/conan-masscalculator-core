pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Environment setup') {
            steps {
                sh "sudo tools/installers/essentials.sh"
            }
        }
        stage('Create') {
            steps {
                sh "conan create all/ --version 0.1.0 --user masscalculator --channel stable --build missing"
            }
        }
        stage('Upload') {
            steps {
                echo 'Upload stage is in progress'
            }
        }
    }
}

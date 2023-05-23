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
        stage('Conan Profile Detect') {
            steps {
                sh "sudo tools/installers/essentials.sh"
            }
        }
        stage('Conan Create') {
            steps {
                sh "conan create all/ --version 0.1.0 --user masscalculator --channel stable --build missing"
            }
        }
        stage('Conan Upload') {
            steps {
                echo 'Upload to conancenter is in progress'
            }
        }
    }
}

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
                sh "conan profile detect"
            }
        }
        stage('Conan Create') {
            steps {
                sh "conan create all/ --version 0.2.0 --user masscalculator --channel stable --build missing"
            }
        }
        stage('Conan Upload') {
            steps {
                echo 'Upload to conancenter is in progress'
            }
        }
    }
}

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
                script {
                    def profile_path = '/var/lib/jenkins/.conan2/profiles/default'
                    if (fileExists(profile_path)) {
                        sh "Profile '/var/lib/jenkins/.conan2/profiles/default' already exists"
                    } else {
                        sh "conan profile detect"
                    }
                }
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

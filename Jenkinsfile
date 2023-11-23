pipeline {
    agent {
        node {
            label 'docker-agent-python'
        }
    }
    triggers {
        pollSCM '* * * * *'
    }
    parameters{
        string(name: 'welcome-text', defaultValue: 'Have fun reading the logs!\n', description: "Welcome text to display in the beginning of the build logs")

        choice(name: 'banner-type', choices: ["None", "Single", "Double", "Framed"], description: "Type of the banner display in the build logs")

        file(name: 'file-params/banner-pattern', description: 'Banner to be displayed in build logs for fun')
    }
    stages {
        stage('Banner'){
            steps {
                sh '''
                    if [ $banner-type != 'None']; then
                        cat file-params/banner-pattern
                    fi
                    echo $welcome-text
                '''
            }
        }
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                cd myapp
                pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                cd myapp
                /home/jenkins/.local/bin/pytest
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}
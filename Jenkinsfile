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
        string(name: 'WELCOME_TEXT', defaultValue: 'Have fun reading the logs!\n', description: "Welcome text to display in the beginning of the build logs")

        choice(name: 'BANNER_TYPE', choices: ["None", "Single", "Double", "Framed"], description: "Type of the banner display in the build logs")

        base64File(name: 'BANNER')
    }
    stages {
        stage('Banner'){
            steps {
                script{

                    params.each() { param, value ->
                        print "Parameter: ${param}, Value: ${value}"
                    }
                }

                sh'''#!/bin/bash
                    echo ${WELCOME_TEXT}
                    echo ${BANNER_TYPE}

                    if [ $BANNER_TYPE != '' -a $BANNER_TYPE != 'None' ]; then
                        echo ${BANNER} | base64 -d
                    fi
                    echo ${WELCOME_TEXT}
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
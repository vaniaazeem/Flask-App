pipeline {
    agent any

    environment {
        VENV = "venv"
        DEPLOY_DIR = "/tmp/flask_deployment"
    }

    stages {

        stage('Clone Repository') {
            steps {
                echo 'Cloning Flask application from GitHub...'
                git branch: 'main',
                    url: 'https://github.com/vaniaazeem/flask-app.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                sh '''
                python3 -m venv $VENV
                . $VENV/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                pip install pytest
                '''
            }
        }

        stage('Run Unit Tests (Simulated)') {
            steps {
                echo 'Running basic application test...'
                sh '''
                . $VENV/bin/activate
                python -c "import app; print('App imported successfully')"
                '''
            }
        }

        stage('Build Application') {
            steps {
                echo 'Building application...'
                sh '''
                mkdir -p build
                cp app.py requirements.txt build/
                '''
            }
        }

        stage('Deploy Application (Simulation)') {
            steps {
                echo 'Deploying application...'
                sh '''
                mkdir -p $DEPLOY_DIR
                cp -r build/* $DEPLOY_DIR
                echo "Application deployed to $DEPLOY_DIR"
                '''
            }
        }
    }

    post {
        success {
            echo 'CI/CD Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check logs.'
        }
    }
}

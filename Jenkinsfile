pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat '''
                python -m venv venv
                venv\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Basic Test') {
            steps {
                bat '''
                venv\\Scripts\\activate
                python -c "import app; print('App loaded successfully')"
                '''
            }
        }

        stage('Build Application') {
            steps {
                bat '''
                mkdir build
                copy app.py build\\
                copy requirements.txt build\\
                '''
            }
        }

        stage('Deploy Application (Simulation)') {
            steps {
                bat '''
                mkdir deploy
                xcopy build deploy /E /Y
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}

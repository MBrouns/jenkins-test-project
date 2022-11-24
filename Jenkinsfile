// jenkins.io/doc/book/pipeline/jenkinsfile/

class Venv {
    private location
    private stage

    public Venv(stage, location) {
        this.location = location
        this.stage = stage
    }
    def setup() {
        stage.sh('/usr/local/bin/python -m venv ' + location)
    }

    def runModule(String args) {
        stage.sh(location + '/bin/python -m ' + args)
    }
}

node {
    docker.image('python:3.8').inside() {
        checkout scm
        def venv = new Venv(this, '/home/jenkins-agent/workspace/github-test/venv')
        sh('python --version')


        stage('Setup Python') {
            venv.setup()
        }
        stage('Install') {
            venv.runModule('pip install -e ".[all]"')
        }
        tests = [
            "pytest": {
                venv.runModule('pytest')
            },
            "typing": {
                venv.runModule('mypy src/')
            },
            "linting": {
                venv.runModule('flake8 src/')
            }
        ]
        parallel tests
        echo "running on branch ${env.BRANCH_NAME}"
        if (env.BRANCH_NAME == 'main'){
            timeout(time: 10, unit: 'SECONDS') {
            // Note that input ties up an executor slot!
            input 'Continue?'
            }
        }
        stage('Deploy') {
            echo "Deploying"

        }

    }
}

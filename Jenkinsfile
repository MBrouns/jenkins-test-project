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
        def venv = new Venv(this, '/var/jenkins_home/workspace/jenkins-testproject/venv')
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
    }
}

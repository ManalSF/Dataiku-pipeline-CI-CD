pipeline {
    agent any
    
    environment {
        API_SERVICE_ID = "defect_detection"
        API_ENDPOINT_ID = "predict_defect"
        DESIGN_URL = "http://35.181.135.32:16000/"
        DESIGN_API_KEY = "2GEJJFF192HSWH3JRMKFXYDRBEVWQ559"
        API_DEV_INFRA_ID = "api-node-dev"
        API_PROD_INFRA_ID = "api-node-prod"
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/ManalSF/Jenkins-dataiku-python-test.git']])
            }
        }
        
        stage('Build') {
            steps {
                // Build steps here (e.g., compiling code, running tests)
                echo 'Hello'
            }
        }
        
        stage('Create API Package') {
            steps {
                script {
                    bat """
                    curl -X POST ^
                    -H "Content-Type: application/json" ^
                    -H "Authorization: Bearer 2GEJJFF192HSWH3JRMKFXYDRBEVWQ559" ^
                    -d "{\"serviceId\": \"defect_detection\", \"endpoint_id\": \"predict_defect\"}" ^
                    http://35.181.135.32:16000/projects/STAGETEST2/api-designer/v6/
                    """
                }
            }
        }
        
        // API request to create a package
       stage('Create API Package') {
            steps {
                script {
                    def apiService = new com.dataiku.dip.api.DSSAPIService()
                    def packageParams = [
                        "serviceId": "defect_detection",
                        "endpointId": "predict_defect"
                    ]
                    def packageResponse = apiService.create_package(packageParams)
                    
                    if (packageResponse.status == 201) {
                        println "API package created successfully."
                    } else {
                        println "Failed to create API package. Status code: ${packageResponse.status}"
                    }
                }
            }
        }
        
        stage('Dataiku API Testing') {
            steps {
                // Make API calls to Dataiku for testing

                // Example: Trigger a Dataiku scenario
                bat """
                    curl -X POST ^
                    -H "Content-Type: application/json" ^
                    -H "Authorization: Bearer 2GEJJFF192HSWH3JRMKFXYDRBEVWQ559" ^
                    -d "{\"service_id\": \"defect_detection\", \"endpoint_id\": \"predict_defect\"}" ^
                    http://35.181.135.32:16000/v2/scenarios
                """
                
                // Example: Deploy to development infrastructure
                bat """
                    curl -X POST ^
                    -H "Content-Type: application/json" ^
                    -H "Authorization: Bearer 2GEJJFF192HSWH3JRMKFXYDRBEVWQ559" ^
                    -d "{\"infraId\": \"api-node-dev\", \"serviceId\": \"defect_detection\"}" ^
                    http://35.181.135.32:16000/v2/infrastructures/deploy
                """
                bat """
                    curl -X POST ^
                    -H "Content-Type: application/json" ^
                    -H "Authorization: Bearer 2GEJJFF192HSWH3JRMKFXYDRBEVWQ559" ^
                    -d "{\"infraId\": \"api-node-prod\", \"serviceId\": \"defect_detection\"}" ^
                    http://35.181.135.32:16000/v2/infrastructures/deploy

                """
            }
        }
    }
}
        
       


pipeline {
    agent any
	
	environment {
				PROJECT_ID = 'kubernetes-project-378913'
                CLUSTER_NAME = 'jenkin-cluster'
                LOCATION = 'asia-east1-a'
                CREDENTIALS_ID = 'kubernetes'
				DOCKERHUB_CREDENTIALS = credentials('dockerhub')
				GCLOUD_CREDS=credentials('gcloud-creds')
			}
	
    stages {
		stage('Checkout Source') {
      		steps {
        		git url:'https://github.com/malamcsc/django-todo-develop.git', branch:'master', credentialsId: 'github'
      		}
    	}
	    
	    stage("Build image") {
            steps {
                script {
                    myapp = docker.build("gcr.io/kubernetes-project-378913/test-project-images:${env.BUILD_ID}")
                }
            }
        }
	    
	    stage('Login and Dcoker push') {
          steps {
                sh ''' 
        		    gcloud auth activate-service-account --key-file="$GCLOUD_CREDS"
        		    docker login -u _json_key --password-stdin https://gcr.io < "$GCLOUD_CREDS"
                    sudo docker push gcr.io/kubernetes-project-378913/test-project-images:"$BUILD_ID" 
                  '''
                
				}
		    }
           
		
	    
	    stage('Deploy to K8s') {
		    steps{
			    echo "Deployment started ..."
				sh "sed -i 's/tagversion/${env.BUILD_ID}/g' deploy_gcp_infra.yaml"
			    step([$class: 'KubernetesEngineBuilder', projectId: env.PROJECT_ID, clusterName: env.CLUSTER_NAME, location: env.LOCATION, manifestPattern: 'deploy_gcp_infra.yaml', credentialsId: env.CREDENTIALS_ID, verifyDeployments: true])
			    echo "Deployment Finished ..."
		    }
	    }
    }
}
pipeline {

  agent any
  environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
    }

  stages {

    stage('Checkout Source') {
      steps {
        git url:'https://github.com/malamcsc/kubernetes_project.git', branch:'master', credentialsId: 'github'
      }
    }

      stage('Checkout') {
        steps { git branch: 'master', credentialsId: 'github', url: 'https://github.com/malamcsc/kubernetes_project.git'
        }
      }
      stage("Build image") {
            steps {
                script {
                    myapp = docker.build("malamcsc/kubernetes_project:${env.BUILD_ID}")
                }
            }
        }
    
         
        stage('Login and Dcoker push') {
          steps {
            script{
                  withDockerRegistry([ credentialsId: "dockerhub", url: "" ]){
                  myapp.push("${env.BUILD_ID}") }
                  }
		          }
           }
         
    stage('Deploy App') {
      steps { 
        withKubeConfig([credentialsId: 'mykubeconfig']){
        sh "sed -i 's/tagversion/${env.BUILD_ID}/g' deploy.yaml"
        sh 'curl -LO "https://storage.googleapis.com/kubernetes-release/release/v1.20.5/bin/linux/amd64/kubectl"'
        sh 'chmod u+x ./kubectl'
        sh "./kubectl apply -f deploy.yaml"
        }
        
      }
    }

    // stage('Deploy App') {
    //   steps {
    //     sh "docker run --name k8s-app-v1 -d -p 5000:5000 malamcsc/kubernetes_project:${env.BUILD_ID}"
    //     }
        
    //   }
    

    
  }

}
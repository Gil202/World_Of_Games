pipeline { 
    environment { 
        registry = "gil202/wog-image" 
        registryCredential = 'bb3d7740-c077-4a1b-9ba7-1127b48217a1' 
        customImage = '' 
    }
    agent any 
    stages { 
        stage('Cloning our Git') { 
            steps { 
                git 'https://github.com/Gil202/World_Of_Games' 
            }
        } 
        stage('Building our image') { 
            steps { 
                script { 
                    customImage = docker.build("gil202/wog-image:${env.BUILD_ID}") 
                }
            } 
        }
        stage('Deploy our image') { 
            steps { 
                script { 
                    docker.withRegistry('', registryCredential)  { 
                        customImage.push() 
                    }
                } 
            }
        } 
        stage('Cleaning up') { 
            steps { 
                sh "docker rmi $registry:$BUILD_ID" 
            }
        } 
    }
}

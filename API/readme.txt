# Rebuild Docker image: location, projectID, repo, image name:tag
docker build -t lingomalay-kedah:latest .

docker tag lingomalay-kedah:latest asia-southeast1-docker.pkg.dev/lingomalay/lingomalay/lingomalay-kedah

# Push to Artifact Registry, Can also push to docker hub
docker push asia-southeast1-docker.pkg.dev/lingomalay/lingomalay/lingomalay-kedah

# check artifact registry
gcloud artifacts docker images list asia-southeast1-docker.pkg.dev/lingomalay/lingomalay

# delete from artifact registry
gcloud artifacts docker images delete asia-southeast1-docker.pkg.dev/lingomalay/lingomalay/lingomalay-api:kedah --quiet

# Redeploy to Cloud Run
gcloud run deploy lingomalay-kedah \
  --image asia-southeast1-docker.pkg.dev/lingomalay/lingomalay/lingomalay-kedah \
  --region asia-southeast1 \
  --memory 16Gi \
  --cpu 4 \
  --timeout 300 \
  --concurrency 1 \
  --allow-unauthenticated

gcloud ai models upload \
  --region=asia-southeast1 \
  --display-name=lingomalay-kedah \
  --container-image-uri=asia-southeast1-docker.pkg.dev/lingomalay/lingomalay/lingomalay-kedah \
  --container-port=8080 \
  --container-predict-route=/transcribe \
  --container-health-route=/


# build local
docker build -t lingomalay-kelantan:latest .

# run local
docker run -p 8081:8080 lingomalay-kelantan:latest

# run local detach
docker run -d -p 8081:8080 lingomalay-kelantan:latest

# check local
docker ps

# stop local
docker stop lingomalay-api:kelantan

# ngrok help
ngrok config add-authtoken <TOKEN_FROM_ACCOUNT_1>
ngrok http http://localhost:8080



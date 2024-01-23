#install the nodejs and npm

sudo yum update -y
sudo yum install -y nodejs npm

node_version=$(node -v)
npm_version=$(npm -v)

echo "Node version:"$node_version
echo "npm_version:"$npm_version

artifact_url="https://node-envvars-artifact.s3.eu-west-2.amazonaws.com/bootcamp-node-envvars-project-1.0.0.tgz"
artifact_file="bootcamp-node-envvars-project-1.0.0.tgz"

curl -O $artifact_url

ls -lh $artifact_file
tar -xzvf $artifact_file

cd package
npm install
node server.js
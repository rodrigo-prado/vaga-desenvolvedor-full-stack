# vaga-desenvolvedor-full-stack
Repository created for the job selection process (Full Stack Developer Job).
The objective is to evaluate skills in application development.

# Start docker
sudo systemctl start docker

# Build docker images
sudo docker build --rm -f "DockerfilePostgreSQL" -t get-all-links-database:latest .

# Start DataBase
docker run --name get-all-links-database -e POSTGRES_PASSWORD=postgres -d get-all-links-database
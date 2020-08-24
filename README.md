# vaga-desenvolvedor-full-stack
Repository created for the job selection process (Full Stack Developer Job).
The objective is to evaluate skills in application development.

# Start the docker
```Shell
sudo systemctl start docker
```

# Build the docker images
```Shell
sudo docker build --rm -f "DockerfilePostgreSQL" -t get-all-links-database:latest .
sudo docker build --rm -f "DockerfileApplication" -t collect_all_links:latest .
```

# Start the DataBase
```Shell
docker run --name get-all-links-database -e POSTGRES_PASSWORD=postgres -d get-all-links-database
```

# Run the application
```Shell
docker run -it --link get-all-links-database:get-all-links-database collect_all_links
```
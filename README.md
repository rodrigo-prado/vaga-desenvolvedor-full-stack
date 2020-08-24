# vaga-desenvolvedor-full-stack
Repository created for the job selection process (Full Stack Developer Job).
The objective is to evaluate skills in application development.

# Start the docker
```Shell
sudo systemctl start docker
```

# Build the docker images
```Shell
sudo docker build --rm -f "DockerfilePostgreSQL" -t collect-all-links-database:latest .
sudo docker build --rm -f "DockerfileApplication" -t collect_all_links:latest .
```

# Run the application using Docker

## Start the Database
```Shell
docker run --name collect-all-links-database -e POSTGRES_PASSWORD=postgres -d collect-all-links-database
```

## Execute tests and one example
```Shell
docker run -it --link collect-all-links:collect-all-links-database collect_all_links
```

## Execute passing some other initial web link (change http://google.com for some other web link)
```Shell
docker run -it --link collect-all-links-database:collect-all-links collect_all_links python ./src/collect_all_links.py http://www.google.com --limit 100
```
--limit avoid that the execution goes on FOREVER

# Run the application in the IBM Cloud

## Connect to the appropriate IBM Cloud instance
```Shell
ibmcloud login -a cloud.ibm.com -r eu-de -g Default --apikey "nmsWhc9kCJvMkk2_wD--ndje4ztopFVrA_7hPHKL1Kho"
```

## Retrieve cluster configuration and set Kubernetes context
```Shell
ibmcloud ks init
ibmcloud ks cluster config --cluster bt1tb0qf0uo8ia7b4h70
```

## Execute tests and one example
```Shell
kubectl exec collect-all-links -- ./run_all.sh
```

## Execute passing some other initial web link (change http://google.com for some other web link)
```Shell
kubectl exec collect-all-links -c collect-all-links-application -- python ./src/collect_all_links.py http://www.google.com --limit 100
```
--limit avoid that the execution goes on FOREVER

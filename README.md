# harmonic_filter

run with docker example:
#dockerhub:
docker run -d --name harmonic_filter -p 5000:5000 slavarub/harmonic_filter:final

#docker compose:
go to root folder of the project (verify harmonic_filter.tar exist)
run command:
1. docker load -i harmonic_filter.tar (in order to load image)
2. docker-compose start harmonic-filter (will start the service)

docker image can be found on root folder:
harmonic_filter.tar
or in dockerhub:
slavarub/harmonic_filter:final


API request to filter file (postman collection could be found inside root folder of the container: endpoint: localhost:5000/harmonic_filter
input example:
{
    "sample_rate": 8000,
    "base_freq": 50,
    "num_harmonics": 10,
    "samples":[0.123456, 0.987653, -0.8542635, -0.23568, 0.123456, 0.987653, -0.8542635, -0.23568, 0.123456, 0.987653, -0.8542635, -0.23568, 0.123456, 0.987653, -0.8542635, -0.23568]
}

output will be list of filtered samples
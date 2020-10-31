# harmonic_filter

run with docker example:

#dockerhub:
docker run -d --name harmonic_filter -p 5000:5000 slavarub/harmonic-filter:final

#docker compose:
run command:
1. download docker image - https://drive.google.com/file/d/1kRpzvWZ-XvP_GOt4AqGuvhq5PnzpQPkh/view?usp=sharing
2. docker load -i harmonic_filter.tar (in order to load image)
3. docker-compose start harmonic-filter (will start the service)

docker image can be downloaded from google drive link:
 https://drive.google.com/file/d/1kRpzvWZ-XvP_GOt4AqGuvhq5PnzpQPkh/view?usp=sharing

in orde rto pull image from dockerhub:
docker pull slavarub/harmonic-filter:final

#API request
API request to filter file (postman collection could be found inside root folder of the container: endpoint: localhost:5000/harmonic_filter
input example:
{
    "sample_rate": 8000,
    "base_freq": 50,
    "num_harmonics": 10,
    "samples":[0.123456, 0.987653, -0.8542635, -0.23568, 0.123456, 0.987653, -0.8542635, -0.23568, 0.123456, 0.987653, -0.8542635, -0.23568, 0.123456, 0.987653, -0.8542635, -0.23568]
}

output will be list of filtered samples

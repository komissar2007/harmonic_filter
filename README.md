# harmonic_filter

run with docker example: folder_with_wav - path to you wav files

docker run -d --name harmonic_filter -p 5000:5000 -v "C:/Dev/filter_example/files:/harmonic_filter/file" -v "C:/Dev/filter_example/filtered:/harmonic_filter/filtered" slavarub/harmonic_filter

API request to filter file (postman collection could be found inside root folder of the container: endpoint: localhost:5000/filter input example: { "file_name": "in.wav", "base_freq": 50, "harmonics": 10 }

this should build new filtered wav file inside filtered folder
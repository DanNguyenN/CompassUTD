# Langchain tools

### Prepare
This repository contain the agent tools API/microservices that will allow the Langchain agent to 
perform Google Programmable Search Engine on utdallas.edu.

1. Get the API key to perform the search. Then create 3 search engines and save individual `Search Engine ID`:

|                | Course Search <img width=200/>| Degree Search <img width=200/>| Random Search <img width=200/>|
|----------------|--------------------------|-------------------------------|-------------------------------|
| Search sites   | - catalog.utdallas.edu/<br/>\*/\*/courses/***** | - catalog.utdallas.edu/<br/>202*/\*/programs/\*/*  | - catalog.utdallas.edu/\*/\*/home/* <br/> - bpb-us-e2.wpmucdn.com/sites.utdallas.edu/* <br/> - \*.utdallas.edu/* |
| Excluded sites | - catalog.utdallas.edu/<br/>\*/\*/courses/school/*  | *None* | - dox.utdallas.edu/syl*<br/>- catalog.utdallas.edu/* |

2. Then create a `.env` file to store 4 variable environment in the `/app` folder as such:
```aidl
GOOGLE_SEARCH_API = YOUR_API_KEY
COURSE_SEARCH_ID = YOUR_SEARCH_ENGINE_ID
DEGREE_SEARCH_ID = YOUR_SEARCH_ENGINE_ID
RANDOM_SEARCH_ID = YOUR_SEARCH_ENGINE_ID
```

3. Now you can run the container. You should have the following installed:
>- Google Cloud CLI
>- Docker
>- Python 3.6 or later

4. Edit the `image` and the `region` in the `build.yaml` to match location of your image

5. Authenticate the google cloud CLI to access GCP
```
gcloud auth login
```

6. Deploy it using the command below. If you make some changes, just rerun this command:
```
gcloud builds submit --config build.yaml
```
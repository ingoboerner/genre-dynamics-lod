# genre-dynamics-lod

## Run infrastructure (JENA Fuseki, SKOSMOS)

With Docker installed: In the folder `src/docker` execute
`docker compose up`

Skosmos is running at http://localhost:9090
Jena Fuseki at http://localhost:9030 (use "admin"/"querty")

## Python stuff (folder skos-tools)

`python3 -m venv venv`
`source venv/bin/activate` 
`pip install -r requirements.txt`


This setup was presented at the conference [Linked Open Data and Literary Studies](https://www.temporal-communities.de/events/2024/conference-linked-open-data.html) at the FU Berlin on Nov 20, 2024.

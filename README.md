# elasticsearch_grafana_docker
use grafana with elasticsearch to visualize data

* elasticsearch basic:	

		- index + type + doc

		- api: PUT POST GET
			
* tools: postman to use es api

## User Stories

* [x] Setup elasticsearch docker container
	* [x] Map port from docker container
	* [x] Map data storage in local
	
	docker run -p 9200:9200 -v ./data:/usr/share/elasticsearch/data --name=elasticsearch myelasticsearch

* [ ] Tool to import/index data to es
	
	docker run -p 9200:9200 -v /Users/lamdo/Documents/myProjs/docker/elasticsearch_grafana_docker/data:/usr/share/elasticsearch/data --name=elasticsearch myelasticsearch



## Notes
https://www.webcodegeeks.com/devops/docker-elasticsearch-tutorial/

https://github.com/deviantony/docker-elk

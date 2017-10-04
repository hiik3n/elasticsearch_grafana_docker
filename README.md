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
	* [x] Pre-define (configure) the format of data on es
	
	docker run -p 9200:9200 -v ./data:/usr/share/elasticsearch/data --name=elasticsearch myelasticsearch
	
	curl localhost:9200
	
	PUT localhost:9200/index	>> create Index
	
	PUT localhost:9200/index/_mapping/type	>> mapping properties of type of index (type of properties is important when link to grafana)
	
	 {
	     "properties": {
	      	  "created_at" : {
		    "type" : "date"
		  },
		  "device_id" : {
		    "type" : "keyword"
		  },
		  "data" : {
		    "type" : "integer"
		  },
		  "timestamp" : {
		    "type" : "date",
		    "format" : "epoch_millis"
		  }
	     }
	 }
	 
	PUT localhost:9200/index/type/_mapping		>> see the mapping index and type
	
	curl localhost:9200/index/type -d '{"msg":1}'
	
	curl localhost:9200/_search?pretty=true

	localhost:9200/_cat/indices

	curl localhost:9200/_mapping?pretty=true
	
	curl localhost:9200/index/type/_mapping?pretty=true

* [x] Tool to import/index data to es

* [ ] Setup Grafana for visualize data
	
		elastic-changeme
		
		docker run -d --name=grafana -p 3000:3000 grafana/grafana
		
		


## Notes
https://www.webcodegeeks.com/devops/docker-elasticsearch-tutorial/

https://github.com/deviantony/docker-elk

https://stackoverflow.com/questions/8498371/curl-get-and-x-get

https://blog.codeship.com/orchestrate-containers-for-development-with-docker-compose/

http://docs.grafana.org/features/datasources/elasticsearch/

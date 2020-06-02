test:
	# Test the simple hello_world
	# py.test ./test_hello_world.py
	# Test the simple_http_server
	py.test ./test_simple_http_server.py

build: 
	echo "Build Phase"
	if [ "${BUILD_NUMBER}" != "" ]; \
	then \
		docker build -t hello_world_app:${BUILD_NUMBER} -f docker/Dockerfile . ; \
		docker tag hello_world_app:${BUILD_NUMBER} zioalex/hello_world_app:${BUILD_NUMBER} ; \
		docker tag hello_world_app:${BUILD_NUMBER} zioalex/hello_world_app:latest ; \
	else \
		docker build -t hello_world_app:latest -f docker/Dockerfile . ; \
		docker tag hello_world_app:latest zioalex/hello_world_app:latest ; \
	fi;

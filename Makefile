test:
	py.test ./test_hello_world.py

build: 
	if [ "${BUILD_NUMBER}" != "" ]; \
	then \
		docker build -t hello_world_app:${BUILD_NUMBER} -f docker/Dockerfile . ; \
	else \
		docker build -t hello_world_app:latest -f docker/Dockerfile . ; \
	fi;

user=aequitas
name=http-resource

docker=docker
tag = $(user)/$(name)
dockerfile = Dockerfile

.PHONY: test

push: build
	$(docker) push $(user)/$(name)

build:
	$(docker) build -t $(tag) -f $(dockerfile) .

test: tag=$(user)/$(name)-test
test: dockerfile=Dockerfile.tdd
test: build
	$(docker) run $(args) \
		-e HIPCHAT_TOKEN=${HIPCHAT_TOKEN} \
		$(user)/$(name)-test

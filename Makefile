IMAGE_NAME=pjatk_nlp

build:
	docker build -t $(IMAGE_NAME) .

dev:
	docker run --rm -ti \
		-v $(PWD)/:/project \
		-w="/project" \
		$(IMAGE_NAME)

lab:
	docker run --rm -ti \
		-p 8888:8888 \
		-v $(PWD)/:/project \
		-w="/project" \
		$(IMAGE_NAME) \
		jupyter lab --ip=0.0.0.0 --port=8888 --allow-root --no-browser

test:
	python3 -m pytest tests/

data/README.txt:
	$(eval FILENAME := data/poleval_data.zip)
	wget -O $(FILENAME) http://poleval.pl/task6/task_6-1.zip
	unzip $(FILENAME) -d data/
	@echo "Retrieved at: $(shell date +%F_%T%Z)"  > data/README.txt
	rm $(FILENAME)
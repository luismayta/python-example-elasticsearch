# Django
MANAGE:=manage.py

django.help:
	@echo '    Django:'
	@echo ''
	@echo '        django                   command=(shell|createsuperuser|migrate|populate|populate_texts)'
	@echo '        django.runserver 	    run server 0.0.0.0 stage=(dev|stage|prod)'
	@echo '        django.gunicorn 	        run server 0.0.0.0 stage=(dev|stage|prod)'
	@echo ''

django: clean
	@if [ -z "${command}" ]; then \
		make django.help;\
	fi
	@if [ -z "${stage}" ] && [ -n "${command}" ]; then \
		$(docker-compose) -f "${PATH_DOCKER_COMPOSE}"/dev.yml run --rm "$(DOCKER_SERVICE)" bash -c "pipenv run python $(MANAGE) ${command}" ; \
	elif [ -n "${stage}" ] && [ -n "${command}" ]; then \
		$(docker-compose) -f "${PATH_DOCKER_COMPOSE}"/"${stage}".yml run --rm "$(DOCKER_SERVICE)" bash -c "pipenv run python $(MANAGE) ${command}"; \
	fi

django.runserver: clean
	@if [ -z "${stage}" ]; then \
		$(docker-compose) -f ${PATH_DOCKER_COMPOSE}/dev.yml run --rm --service-ports $(DOCKER_SERVICE) bash -c "pipenv run python $(MANAGE) runserver 0.0.0.0:${PROJECT_PORT} --noreload" ; \
	else \
		$(docker-compose) -f "${PATH_DOCKER_COMPOSE}"/"${stage}".yml run --rm --service-ports "$(DOCKER_SERVICE)" bash -c "pipenv run python $(MANAGE) runserver 0.0.0.0:${PROJECT_PORT} --noreload"; \
	fi

django.gunicorn: clean
	@if [ -z "${stage}" ]; then \
		$(docker-compose) -f "${PATH_DOCKER_COMPOSE}"/dev.yml run --rm --service-ports "$(DOCKER_SERVICE)" bash -c "pipenv run gunicorn config.wsgi -b 0.0.0.0:${PROJECT_PORT}" ; \
	else \
		$(docker-compose) -f "${PATH_DOCKER_COMPOSE}"/"${stage}".yml run --rm --service-ports "$(DOCKER_SERVICE)" bash -c "pipenv run gunicorn config.wsgi -b 0.0.0.0:${PROJECT_PORT}"; \
	fi

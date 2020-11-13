clean-pyc:
	find . -name "*.pyc" -delete

run-erp: clean-pyc
	DJANGO_SETTINGS_MODULE=simple_bus.settings.erp ./manage.py runserver 8000

run-drive: clean-pyc
	DJANGO_SETTINGS_MODULE=simple_bus.settings.drive ./manage.py runserver 8001

run-tablet: clean-pyc
	DJANGO_SETTINGS_MODULE=simple_bus.settings.tablet ./manage.py runserver 8002

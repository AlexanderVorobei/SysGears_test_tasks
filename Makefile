.PHONY: all \
		setup \
		lint \
		task1 \
		task2 \
		task3

venv/bin/activate: ## alias for virtual environment
	python3 -m venv venv

setup: venv/bin/activate ## project setup
	. venv/bin/activate; pip install pip wheel setuptools
	. venv/bin/activate; pip install -r requirements.txt

task1: venv/bin/activate ## run task1
	. venv/bin/activate; python3 task_1/task_1.py

task2: venv/bin/activate ## run task2
	. venv/bin/activate; python3 task_2/task_2.py

task3: venv/bin/activate ## run task3
	. venv/bin/activate; python3 task_3/task_3.py

lint:
	. venv/bin/activate; flake8 --config=./.config/.flake ./

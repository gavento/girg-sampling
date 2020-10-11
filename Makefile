.PHONY: clean

clean:
	rm dist/ build/ girg_sampling/_girgs_cpplib -rf

build:
	poetry build

test:
	poetry install
	poetry run pytest .

install: # poetry install
	poetry install

brain-games: # run brain-games
	poetry run brain-games

build: # build the package
	poetry build

publish: # publishing a build
	poetry publish --dry-run

package-install: # installing the package
	python3 -m pip install --user dist/*.whl

package-reinstall: #reinstalling the package
	python3 -m pip install --user dist/*.whl --force-reinstall

lint: # run linter
	poetry run flake8 brain_games
test: clean-cover
	nosetests --with-coverage --cover-html --cover-package=cubemu

clean-cover:
	rm -rf cover

test-pdb:
	nosetests --pdb

.PHONY: test

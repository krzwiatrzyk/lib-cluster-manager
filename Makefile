SHELL=bash

install-all: install-taskfile

.ONESHELL:

install-taskfile:
	sudo sh -c "$$(curl --location https://taskfile.dev/install.sh)" -- -d -b /usr/local/bin
	mkdir ~/.statusfiles

add-submodule:
	git submodule add https://github.com/krzwiatrzyk/k3d-demos
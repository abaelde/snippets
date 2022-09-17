#!/bin/sh

# Functions
get_help(){
	echo "little script to install python dependencies for the TSE project";
	echo "please remember to activate your virtual environment before running this script";
	echo "Flags:";
	echo "-d	dev flag, install dev dependencies as well";
	echo "-g	gpu flag, installs gpu libraries for ML modules";
}

# defaults
dev=0
gpu=0

# shell options
while getopts dgh flag; do
	case $flag in
		d) dev=1;;
		g) dev=1; gpu=1;;
		h) get_help; exit 0;;
	esac
done

echo "using `which pip`"
echo "are you sure you sourced your venv correctly?"
read -p "[press ENTER to continue, Ctrl-c to exit]" output

echo "[UPGRADING PIP]"
pip install --upgrade pip || exit 1;

echo "[INSTALLING REPO]"
pip install -e . || exit 1;

echo "[INSTALLING REQUIREMENTS]"
pip install -r requirements.txt || exit 1;

echo "[INSTALLING PRECOMMIT HOOKS]"
pre-commit install 

echo "[INSTALL COMPLETE]"

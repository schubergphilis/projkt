#!/usr/bin/env bash

#
# DIRENV
#

# vscode
if [ -d /workspaces ]; then
    direnv allow /workspaces/*
fi

# jetbrains
if [ -d /IdeaProjects ]; then
    direnv allow /IdeaProjects/*
fi

#
# DOCKER
#

sudo chown root:docker /var/run/docker.sock
sudo chmod g+w /var/run/docker.sock

#
# GIT
#

# vscode
if [ -d /workspaces ]; then
    ls -d /workspaces/* | xargs git config --global --add safe.directory
fi

# jetbrains
if [ -d /IdeaProjects ]; then
    ls -d /IdeaProjects/* | xargs git config --global --add safe.directory
fi

#
# STARSHIP
#

starship preset plain-text-symbols -o ~/.config/starship.toml
starship config container.disabled true

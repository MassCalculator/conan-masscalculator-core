# Conan Recipe for masscalculator-core

[![Build Status](https://jenkins.mergimhalimi.com/buildStatus/icon?job=conan-masscalculator-core%2Fmaster)](https://jenkins.mergimhalimi.com/job/conan-masscalculator-core/job/master/)
[![Conan Create](https://github.com/MassCalculator/conan-masscalculator-core/actions/workflows/conan-create.yml/badge.svg?branch=master)](https://github.com/MassCalculator/conan-masscalculator-core/actions/workflows/conan-create.yml)

This is a Conan recipe for `masscalculator-core`. Below, you can find instructions for building and uploading `masscalculator-core` to the Artifactory.

> Note: The `conancenter` will be used as the Artifactory.

## Create the Conan package

`conan create` builds a binary package for the recipe (conanfile.py). It uses the specified configuration (settings) in `.conan/profiles/default`.

```bash
conan create all/ --version 0.2.0 --user masscalculator --channel stable --build missing
```

> Note: The command above uses the specified settings in .conan/profiles/default.

## Display available package recipes and binaries

`conan search` searches for package recipes and binaries in the local cache or a remote. If no remote is specified, only the local cache is searched.

```bash
$ conan search masscalculator-core

conancenter
  masscalculator-core
    masscalculator-core/0.2.0
```

## Upload conan package to artifactory

`conan upload` uploads a recipe and binary packages to a remote.

```bash
conan upload masscalculator-core/0.2.0@masscalculator/stable -r conancenter
```

## Requirements

- Conan >= 2.0.2

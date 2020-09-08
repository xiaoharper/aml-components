# Module overview

## Overview of pipeline and module

A pipeline is a description of a machine learning (ML) workflow, including all of the modules of the workflow and how they work together. The pipeline includes the definition of the inputs (parameters) required to run the pipeline and the inputs and outputs of each module.

A module is an implementation of a pipeline task. A module represents a step in the workflow. Each module takes one or more inputs and may produce one or more outputs. A module consists of an interface (inputs/outputs), the implementation (source code, command-line arguments and environment to run the module ) and metadata (name, description).

A module specification in YAML format describes it's definition.

## Module development lifecycle
Module development is an iterative process. It includes build module, test module, use module in pipeline to solve real business problem and share/reuse of a module. We have provide several CLI commands and SDK functions to boost the efficiency in module development lifecycle.

![module-management-lifecycle](./modules/media/module-lifecycle.png)

### Build a new module

[video-how-to-build-new-module]()

[sample-notebook]()

**CLI commands**

|Command|Purpose|
| -----------| ----------- |
|az ml module init| Initicialze a template dsl module project. The template contains commonly used files in module development, for example source code script, yaml spec, test file.|
|az ml module build|Automatically build yaml spec from source code wrapped as dsl module. |



### Debug module
[video-how-to-debug-module]()

**CLI commands**
- az ml module debug

**SDK function**
- module.from_func()
- module.from_yaml(
- module.run()


### Build pipeline with module
[video-how-to-build-pipeline-with-module]()

dsl.pipeline()

### Debug pipeline
[video-how-to-debug-pipeline]()

pipeline.run()

### Share and resue
[video-how-share-reuse-module]()

az ml pipeline export

Designer UX 

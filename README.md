# aml-components

## Overview

An Azure Machine Learning pipeline is an independently executable workflow of a complete machine learning task. Azure machine learning pipelines provides simplicity, repeatability and quality assurance to manage your machine learning workflow. These benefits become significant as soon as your machine learning project moves beyond pure exploration and into iteration. 

A component is self-contained set of code that performs one step in the ML workflow (pipeline), such as data preprocessing, model training, model scoring and so on. A component is analogous to a function, in that it has a name, parameters, expects certain input and returns some value. Data scientists or developers can wrap their arbitrary code as Azure Machine Learning component by following the component specification .

Currently Azure Machine Learning offers PipelineStep as the basic building block of machine learning pipeline. PipelineStep is one-off wrap of code that cannot be reused across different pipelines. Compare to PipelineStep, component adds following benefits:

- Composability
- Reusability
- Easy development, testing & debug
- Easy pipeline authoring
- Reproducibility
- Sharing & collaboration


Check [pipeline and component overview](./component-pipeline-overview.md) to learn more in detail. 


## Quick start

1. [Use existing component to build a pipeline](https://github.com/Azure/DesignerPrivatePreviewFeatures/blob/master/azureml-modules/samples/get-started.ipynb)

1. Build your own component
    - Read the [component development overview](./component-development-overview.md) to get an overview of features to accelerate component development. 
    - Follow the [tutorial to create your first component](https://github.com/Azure/DesignerPrivatePreviewFeatures/blob/sdkpreview/azureml-modules/samples/create-module-from-existing-python-code.ipynb)


## Samples

to-be-update



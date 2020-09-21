# Component and pipeline overview

## Concept

### Pipeline 

A pipeline is a description of a machine learning (ML) workflow, including all of the components in the workflow and how the components relate to each other in the form of a graph. The pipeline configuration includes the definition of the inputs (parameters) required to run the pipeline and the inputs and outputs of each component.


### Component
A pipeline component is self-contained set of code that performs one step in the ML workflow (pipeline), such as data preprocessing, data transformation, model training, and so on. A component is analogous to a function, in that it has a name, parameters, return values, and a body.

#### Component definition
A component specification in YAML format describes the component for the Azure Machine Learning Pipelines system. A component definition has the following parts:

- **Metadata:** name, description, etc.
- **Interface:**: input/output specifications (name, type, description, default value, etc).
- **Implementation:**: A specification of how to run the component given a set of argument values for the component’s inputs, including source code and environment to run the component. For the complete definition of a component, see the [component specification]().


## Why component?

When you machine learning project get complicated, the complexity of manage it explode. Component can bring you following value. 

- **Composable:** Hide the complexity of code, only expose interface for simplicity. In the meanwhile the code is accessible for component user, make customize development possible. 
-  **Reusable:** Abstract the repetitive logic, which can be reused between different organization/projects.
- **Reproducible:** By capturing all information in component spec, AML Component can be reproduced in different environment/OS?. 
 
- **Share & collaboration:**  Easily share a component by publishing it to component gallery. And build your project on top of other's component.  

[video-show-component-value-prop]() (to-do)

## Consume components in components gallery 

[Component gallery](https://github.com/tichx/azureml-pipeline-components-gallery) is an open community for data scientists to contribute, share, and find machine learning pipelines as well as custom-built components to be used in Azure Machine Learning Studio.

It has more that 50 components for common machine learning tasks. Source code of all components can be find in the gallery. 

Follow [this toturial](./tutorial-use-existing-component-to-build-pipeline.ipynb) (to-do) to learn how to consume a component from the gallery. 


## Build your custom component


- Read the [component development overview](./component-development-overview.md)
- Follow the [tutorial to create your first component](tutorial-create-first-component.ipynb)  

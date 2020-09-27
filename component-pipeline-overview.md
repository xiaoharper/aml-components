# Azure Machine learning pipeline and component overview



## What is Azure Machine Learning pipeline? 

Azure Machine Learning pipelines help you build, optimize, and manage machine learning workflows. These workflows have a number of benefits:

- Simplicity
- Speed
- Repeatability
- Flexibility
- Versioning and tracking
- Modularity
- Quality assurance
- Cost control

These benefits become significant as soon as your machine learning project moves beyond pure exploration and into iteration. Even simple one-step pipelines can be valuable. Machine learning projects are often in a complex state, and it can be a relief to make the precise accomplishment of a single workflow a trivial process.

### What can Azure Machine Learning pipeline do? 

An Azure Machine Learning pipeline is an independently executable workflow of a complete machine learning task. Subtasks are encapsulated as a series of steps within the pipeline. An Azure Machine Learning pipeline can be as simple as one that calls a Python script, so may do just about anything. Pipelines should focus on machine learning tasks such as:

- Data preparation including importing, validating and cleaning, munging and transformation, normalization, and staging
- Training configuration including parameterizing arguments, filepaths, and logging / reporting configurations
- Training and validating efficiently and repeatedly. Efficiency might come from specifying specific data subsets, different hardware compute resources, distributed processing, and progress monitoring
- Deployment, including versioning, scaling, provisioning, and access control


Independent steps allow multiple data scientists to work on the same pipeline at the same time without over-taxing compute resources. Separate steps also make it easy to use different compute types/sizes for each step.

After the pipeline is designed, there is often more fine-tuning around the training loop of the pipeline. When you rerun a pipeline, the run jumps to the steps that need to be rerun, such as an updated training script. Steps that do not need to be rerun are skipped.

With pipelines, you may choose to use different hardware for different tasks. Azure coordinates the various compute targets you use, so your intermediate data seamlessly flows to downstream compute targets.


## What is Azure Machine Learning component? 
A component is self-contained set of code that performs one step in the ML workflow (pipeline), such as data preprocessing, model training, model scoring and so on. A component is analogous to a function, in that it has a name, parameters, expects certain input and returns some value. 
 
Data scientists or developers can wrap their arbitrary code as Azure Machine Learning component by following the component specification .

### Component specification

A component specification in YAML format describes the component in the Azure Machine Learning system. A component definition has the following parts:

- **Metadata:** name, description, etc.
- **Interface:**: input/output specifications (name, type, description, default value, etc).
- **Implementation:**: A specification of how to run the component given a set of argument values for the component’s inputs, including source code and environment required to run the component. 

Refer to [component spec definition](https://github.com/Azure/DesignerPrivatePreviewFeatures/blob/master/azureml-modules/docs/module-spec-definition.md) for more details. 

### What's the benefit of component? 

Currently Azure Machine Learning offers PipelineStep as the basic building block of machine learning pipeline. PipelineStep is one-off wrap of code that cannot be reused across different pipelines. Compare to PipelineStep, component adds following benefits:


-  **Reusable:** Component can be easily reused across different ML pipelines, different ML workspaces, even different organizations.  
- **Reproducible:** By capturing all information in component specification, AML Component can be easily reproduced in different environment. 
-  **Easy development & debug:** Rich SDK and CLI features to make development and debug component much easier. See [component development overview](./component-development-overview.md) to learn more.   
- **Easy management:**  Rich features both in CLI and UI to manage your components.  
- **Componentizable:** This is the native benefit of component. It hides the complicated logic, and only exposes simple interface. So component consumer don't need to worry about implement. They can easily use components build by others. In the meanwhile the ground truth (component specification) of a component is visible, making secondary development easy. 

[video-show-component-value-prop]() (to-do)

## Next steps

### Consume existing components 

[Component gallery](https://github.com/tichx/azureml-pipeline-components-gallery) is an open community for data scientists to contribute, share, and find machine learning pipelines as well as custom-built components to be used in Azure Machine Learning. It has more that 50 components for common machine learning tasks. Source code of all components can be found in the gallery. 

Follow [this toturial](./tutorial-use-existing-component-to-build-pipeline.ipynb) (to-do) to learn how to consume a component from the gallery. 


### Build your custom component


- Read the [component development overview](./component-development-overview.md)
- Follow the [tutorial to create your first component](tutorial-create-first-component.ipynb)  

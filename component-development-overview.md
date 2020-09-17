# Component development overview

In this article you will learn how to develop an Azure Machine Learning component.



A few terminology you will see: 

|Terminology|Description|
| -----------| ----------- |
|YAML spec| component specification in YAML format. It describes all information (interface, implementation, metadata) needed to reproduce a component. YAML spec is needed when register the component to an AML workspace. See example [here](https://github.com/Azure/DesignerPrivatePreviewFeatures/blob/master/azureml-components/docs/component-spec-definition.md).|
|dsl component|A component wrapped by dsl decorator. By using dsl decorator, it's easier to interact with the component. And some component development feature is build on top dsl component. See example [here](). |
|dsl pipeline|A pipeline wrapped by dsl decorator. By using dsl pipeline, it's easier to interact with the pipeline. We recommend to use dsl pipeline to define your pipeline. See example [here](). |




## Component/Pipeline development lifecycle
Component and pipeline development is an iterative process. It includes build component, test component, build pipeline, test pipeline and share/reuse. We have provide several CLI commands and SDK functions to boost the efficiency in the development lifecycle.

![component-management-lifecycle](./components/media/component-lifecycle.png)

### component development

#### Feature overview

|CLI Command|Purpose|
| -----------| ----------- |
|az ml component init| Initialize a template dsl component project. The template contains following useful files in component development process. <br /> - component_name.py: component source code template <br /> - component_name.spec.yaml: component spec in yaml format. Needed to register the component. <br /> - component_name_test.ipynb: template test notebook for the component <br /> - component_name_test.py: unit test template for the component  |
|az ml component build|Automatically build yaml spec from source code that wrapped as dsl component. With this command, customer don't need to edit the yaml spec manually. |

#### Video

[video-how-to-build-new-component]()

#### Sample Notebook

[sample-notebook]()




### component debug


#### Feature overview
|CLI Command|Purpose|
| -----------| ----------- |
|az ml component debug|Debug a component by running it in local container, in which customer can use local debug tools, for example VSCode debugger. Use it in following scenario: <br />  - A component failed in remote run. This command will pull down the image from cloud to debug locally.  <br />  - Test a component with cloud environment before submit to remote run. This command can run a not registered component in local container.|

|SDK function|Purpose|
| -----------| ----------- |
|component.from_func|Load component from a python function. Then you can run the component in local to test.|
|component.from_yaml|Load component from yaml spec. Then you can run the component in local to test. |
|component.run|Run component in your local Python environment or local docker container.|

#### Video

[video-how-to-debug-component]()


#### Sample notebook

[sample-notebook]()



### Build pipeline

#### Feature overview

component SDK provide dsl pipeline wrapper to make it easier to build and interact with pipeline. 

#### Video 

[video-how-to-build-pipeline-with-component]()

#### Sample notebooks

[build-pipeline-basic](https://github.com/Azure/DesignerPrivatePreviewFeatures/blob/sdkpreview/azureml-components/samples/get-started.ipynb)

[create-pipeline-with-subpipeline](https://github.com/Azure/DesignerPrivatePreviewFeatures/blob/sdkpreview/azureml-components/samples/create-pipeline-with-subpipeline.ipynb)

[showcasing-dataset-and-pipeline-parameter](https://github.com/Azure/DesignerPrivatePreviewFeatures/blob/sdkpreview/azureml-components/samples/showcasing-dataset-and-pipelineparameter.ipynb)

[setup-versioned-pipeline-endpoints](https://github.com/Azure/DesignerPrivatePreviewFeatures/blob/sdkpreview/azureml-components/samples/setup-versioned-pipeline-endpoints.ipynb)



### Debug pipeline
#### Feature overview
|SDK function|Purpose|
| -----------| ----------- |
|pipeline.run|It's a light-weight orchestrator in local. In particularly it does following things under the hook: <br /> -  Download remote dataset to local <br /> - Pickup nodes which dependencies are ready, e.g. firstly with nodes that has no dependency node  <br /> - Send the picked nodes in a thread pool (size depends on number of processors on machine by default, user can specify this by max_workers parameter)  <br /> - Execute each node using component.run, which will be executing in separate container/process  <br /> - When node complete, will pickup next ready nodes in downstream to execute, until all nodes in the pipeline complete
|


#### Video
[video-how-to-debug-pipeline]()

#### Sample notebook


[sample-notebook]()


### Share and resue


#### Feature overview
|CLI command|Purpose|
| -----------| ----------- |
|az ml component register|Register a component to an AML workspace. After registration, the component will be shared to all users that have access to the workspace. An it can be consumed both from [AML Designer UI](https://ml.azure.com/) and SDK.|
|az ml pipeline export|Export a pipeline graph to code. See sample [here](). |


#### Video
[video-how-share-reuse-component]()

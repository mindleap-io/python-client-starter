---
title: Getting Started
layout: default
nav_order: 1
---

Mindleap Starter Python Client
==============================
This is the official Python client library for **Mindleap Starter**.

**Mindleap** is a knowledge graph system that allows you to ingest, transform, explore and analyze:
- **any** type of *structured* or *unstructured* data
- from laptop to **planet** scale

**Mindleap Starter** is a limited version, for smaller scale knowledge graphs.

Mindleap Starter is free for **non-commercial** use, making it the ideal alternative to introduce yourself to the world of knowledge graphs.

As you progress into commercial use, Mindleap Starter requires a paid license.

You can use this Python library in conjunction with the Mindleap Starter Web Application to interact with the Mindleap Starter system.

Want to integrate Mindleap in your organization?
------------------------------------------------
Start small:
- Download [Mindleap Starter](https://mindleap.io/mindleap-starter) for non-commercial use
- Use this Python library in [Jupyter Notebook](https://jupyter.org/) or in [your own application code](#example)

Integrate knowledge graphs in your business applications:
- Acquire a paid license for Mindleap Starter
- Use this Python library in [your own application code](#example)

Integrate knowledge graphs in your organization:
- Acquire the enterprise version of [Mindleap](https://mindleap.io/mindleap)
- Use an orchestration framework, such as [Apache NiFi](https://nifi.apache.org/) or [Camunda](https://camunda.com/), to perform tasks in **Mindleap** via client libraries (Python/Java) or the **Mindleap REST API**

Development
-----------
1. Install the mindleap-starter-python-client package:

    ```shell
    pip install mindleap-starter-python-client
    ```

2. Set up your local environment:
- Create a file named `.env` in the project root.
- Fill in the **Mindleap Starter** host url (adjust the port, if necessary)

    ```shell
    MINDLEAP_STARTER_HOST_URL=http://localhost:8090
    ```

Happy coding!

Example
-------
1. Create a simple graph model, using a fluent builder pattern:

    ```python
    from mindleap_starter_python_client.graph_model_service import *
    from mindleap_starter_python_client.services import ResponseStatus
    
    graph_model_service: GraphModelService = GraphModelService()
    
    _SIMPLE_MODEL_ID: UUID = UUID("00000000-0000-0000-0000-000000000001")
    _SIMPLE_MODEL_NAME: str = "Simple Model"
    
    def test_store_simple_graph_model() -> None:
        graph_model: GraphModel = (
            GraphModel()
            .with_id(_SIMPLE_MODEL_ID)
            .with_name(_SIMPLE_MODEL_NAME)
            .add_entity_model(
                EntityModel()
                .with_type_name("person")
                .with_type_label("Person")
                .with_icon_type(IconType.Person)
                .add_property_model(
                    PropertyModel()
                    .with_type_name("name")
                    .with_type_label("Name")
                    .with_value_type(PropertyValueType.String)
                )
                .with_labelling_property_types(["name"])
            )
        )
        response: GraphModelResponse = graph_model_service.store_graph_model(graph_model)
        assert response.status == ResponseStatus.SUCCESS
    ```

2. Create an exploration, using the above graph model:

    ```python
    from mindleap_starter_python_client.exploration_service import *
    from mindleap_starter_python_client.graph_model_service import GraphModelService
    from mindleap_starter_python_client.services import ResponseStatus
    
    graph_model_service: GraphModelService = GraphModelService()
    exploration_service: ExplorationService = ExplorationService()
    
    _EXPLORATION_1_ID: UUID = UUID("00000000-0000-0000-0000-000000000001")
    _EXPLORATION_1_NAME: str = "Exploration 1"
    _SIMPLE_MODEL_ID: UUID = UUID("00000000-0000-0000-0000-000000000001")
    
    def test_store_exploration() -> None:
        graph_model: GraphModel = graph_model_service.get_graph_model_by_id(_SIMPLE_MODEL_ID)
        exploration: Exploration = (
            Exploration()
            .with_id(_EXPLORATION_1_ID)
            .with_name(_EXPLORATION_1_NAME)
            .with_graph_model(graph_model)
            .add_entity(
                Entity()
                .with_entity_type("person")
                .add_property(
                    Property()
                    .with_property_type("name")
                    .with_property_value(StringPropertyValue("James"))
                )
            )
        )
        response: GenericResponse = exploration_service.store_exploration(exploration)
        assert response.status == ResponseStatus.SUCCESS
    ```

Contribution
------------
If you're interested in contributing code to this project, check out the [contribution guidelines]({% link contribution.md %}).

License
-------
The Mindleap Starter Python Client library is open source under the [MIT License]({% link LICENSE %}).

This GitHub Pages site uses the "just-the-docs" Jekyll template,
which is governed by the following [MIT License]({% link LICENSE_just_the_docs %}).

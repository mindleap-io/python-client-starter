---
title: Graph Model
layout: default
nav_order: 2
---

Graph Model
===========
The `graph_model` module contains classes for designing graph models using a fluent builder pattern.

The `graph_model_service` module contains graph model specific services, for interacting with the **Mindleap Starter** system.

You can use the this Python library in conjunction with the Mindleap Starter Web Application.

Examples
--------
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

2. Create a more complex graph model:

    ```python
    from mindleap_starter_python_client.graph_model_service import *
    from mindleap_starter_python_client.services import ResponseStatus
    
    graph_model_service: GraphModelService = GraphModelService()
    
    _COMPLEX_MODEL_ID: UUID = UUID("00000000-0000-0000-0000-000000000002")
    _COMPLEX_MODEL_NAME: str = "Complex Model"
    
    def test_store_complex_graph_model() -> None:
        person_entity_model: EntityModel = (
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
            .add_labelling_property_type("name")
        )
        phone_entity_model: EntityModel = (
            EntityModel()
            .with_type_name("phone")
            .with_type_label("Phone")
            .with_icon_type(IconType.Phone)
            .add_property_model(
                PropertyModel()
                .with_type_name("phone_number")
                .with_type_label("Phone Number")
                .with_value_type(PropertyValueType.String)
            )
            .add_labelling_property_type("phone_number")
        )
        person_relation_model: RelationModel = (
            RelationModel()
            .with_type_name("person_relation")
            .with_type_label("Person Relation")
            .with_from_entity_type("person")
            .with_to_entity_type("person")
            .add_property_model(
                PropertyModel()
                .with_type_name("description")
                .with_type_label("Description")
                .with_value_type(PropertyValueType.String)
            )
            .add_property_model(
                PropertyModel()
                .with_type_name("date")
                .with_type_label("Date")
                .with_value_type(PropertyValueType.Date)
            )
            .with_labelling_property_types(["description", "date"])
        )
        subscriber_relation_model: RelationModel = (
            RelationModel()
            .with_type_name("subscriber_relation")
            .with_type_label("Subscriber")
            .with_from_entity_type("person")
            .with_to_entity_type("phone")
            .add_property_model(
                PropertyModel()
                .with_type_name("date")
                .with_type_label("Date")
                .with_value_type(PropertyValueType.Date)
            )
            .add_labelling_property_type("date")
        )
        graph_model: GraphModel = (
            GraphModel()
            .with_id(_COMPLEX_MODEL_ID)
            .with_name(_COMPLEX_MODEL_NAME)
            .add_entity_model(person_entity_model)
            .add_entity_model(phone_entity_model)
            .add_relation_model(person_relation_model)
            .add_relation_model(subscriber_relation_model)
        )
        response: GraphModelResponse = graph_model_service.store_graph_model(graph_model)
        assert response.status == ResponseStatus.SUCCESS
    ```

3. Get all graph models:

    ```python
    from mindleap_starter_python_client.graph_model_service import *
    from mindleap_starter_python_client.services import ResponseStatus
    
    graph_model_service: GraphModelService = GraphModelService()
    
    def test_get_all_graph_models() -> None:
        response: list[GraphModel] | GraphModelsResponse = graph_model_service.get_graph_models()
        if type(response) is GraphModelsResponse:
            print(response.error_message)
            assert True == False
        else:
            assert len(response) > 0
    ```

4. Get a graph model, by name:

    ```python
    from mindleap_starter_python_client.graph_model_service import *
    from mindleap_starter_python_client.services import ResponseStatus
    
    graph_model_service: GraphModelService = GraphModelService()
    
    _SIMPLE_MODEL_NAME: str = "Simple Model"
    
    def test_get_graph_model_by_name() -> None:
        response: GraphModel | GraphModelResponse = graph_model_service.get_graph_model_by_name(_SIMPLE_MODEL_NAME)
        if type(response) is GraphModelResponse:
            print(response.error_message)
            assert True == False
        else:
            assert response.id == _SIMPLE_MODEL_ID
    ```

5. Get a graph model, by ID:

    ```python
    from mindleap_starter_python_client.graph_model_service import *
    from mindleap_starter_python_client.services import ResponseStatus
    
    graph_model_service: GraphModelService = GraphModelService()
    
    _SIMPLE_MODEL_ID: UUID = UUID("00000000-0000-0000-0000-000000000001")
    
    def test_get_graph_model_by_id() -> None:
        response: GraphModel | GraphModelResponse = graph_model_service.get_graph_model_by_id(_SIMPLE_MODEL_ID)
        if type(response) is GraphModelResponse:
            print(response.error_message)
            assert True == False
        else:
            assert response.id == _SIMPLE_MODEL_ID
    ```

6. Delete a graph model

    ```python
    from mindleap_starter_python_client.graph_model_service import *
    from mindleap_starter_python_client.services import ResponseStatus
    
    graph_model_service: GraphModelService = GraphModelService()
    
    _SIMPLE_MODEL_ID: UUID = UUID("00000000-0000-0000-0000-000000000001")
    
    def test_delete_graph_model() -> None:
        response: GenericResponse = graph_model_service.delete_graph_model(_SIMPLE_MODEL_ID)
        assert response.status == ResponseStatus.SUCCESS
    ```

---
title: Exploration
---

Exploration
===========
The `exploration` module contains classes for creating explorations using a fluent builder pattern.

The `exploration_service` module contains exploration specific services, for interacting with the **Mindleap Starter** system.

You can use this Python library in conjunction with the Mindleap Starter Web Application.

Example
-------
1. Create an exploration, using a fluent builder pattern:

    ```python
    from mindleap_starter_python_client.exploration_service import *
    from mindleap_starter_python_client.graph_model_service import *
    from mindleap_starter_python_client.services import ResponseStatus
    
    graph_model_service: GraphModelService = GraphModelService()
    exploration_service: ExplorationService = ExplorationService()
    
    _EXPLORATION_1_ID: UUID = UUID("00000000-0000-0000-0000-000000000001")
    _EXPLORATION_1_NAME: str = "Exploration 1"
    _COMPLEX_MODEL_ID: UUID = UUID("00000000-0000-0000-0000-000000000002")
    
    def test_store_exploration() -> None:
        graph_model: GraphModel = graph_model_service.get_graph_model_by_id(_COMPLEX_MODEL_ID)
        person_1: Entity = (
            Entity()
            .with_entity_type("person")
            .add_property(
                Property()
                .with_property_type("name")
                .with_property_value(StringPropertyValueHolder("James"))
            )
        )
        person_2: Entity = (
            Entity()
            .with_entity_type("person")
            .add_property(
                Property()
                .with_property_type("name")
                .with_property_value(StringPropertyValueHolder("William"))
            )
        )
        person_3: Entity = (
            Entity()
            .with_entity_type("person")
            .add_property(
                Property()
                .with_property_type("name")
                .with_property_value(StringPropertyValueHolder("Agatha"))
            )
        )
        exploration: Exploration = (
            Exploration()
            .with_id(_EXPLORATION_1_ID)
            .with_name(_EXPLORATION_1_NAME)
            .with_graph_model(graph_model)
            .add_entity(person_1)
            .add_entity(person_2)
            .add_entity(person_3)
            .add_relation(
                Relation()
                .with_relation_type("person_relation")
                .with_from_entity(person_1)
                .with_to_entity(person_2)
                .with_property(
                    Property()
                    .with_property_type("description")
                    .with_property_value(StringPropertyValueHolder("Siblings"))
                )
            )
            .add_relation(
                Relation()
                .with_relation_type("person_relation")
                .with_from_entity(person_1)
                .with_to_entity(person_3)
                .with_property(
                    Property()
                    .with_property_type("description")
                    .with_property_value(StringPropertyValueHolder("Siblings"))
                )
            )
            .add_relation(
                Relation()
                .with_relation_type("person_relation")
                .with_from_entity(person_2)
                .with_to_entity(person_3)
                .with_property(
                    Property()
                    .with_property_type("description")
                    .with_property_value(StringPropertyValueHolder("Siblings"))
                )
            )
        )
        response: GenericResponse = exploration_service.store_exploration(exploration)
        assert response.status == ResponseStatus.SUCCESS
    ```

2. Get all explorations:  

    ```python
    from mindleap_starter_python_client.exploration_service import *
    from mindleap_starter_python_client.services import ResponseStatus
    
    exploration_service: ExplorationService = ExplorationService()
    
    def test_get_all_explorations() -> None:
        response: list[Exploration] | ExplorationsResponse = exploration_service.get_explorations()
        if type(response) is ExplorationsResponse:
            print(response.error_message)
            assert True == False
        else:
            assert len(response) > 0
    ```

3. Get an exploration, by name:

    ```python
    from mindleap_starter_python_client.exploration_service import *
    from mindleap_starter_python_client.services import ResponseStatus
    
    exploration_service: ExplorationService = ExplorationService()
    
    _EXPLORATION_1_NAME: str = "Exploration 1"
    
    def test_get_exploration_by_id() -> None:
        response: Exploration | ExplorationResponse = exploration_service.get_exploration_by_name(_EXPLORATION_1_NAME)
        if type(response) is ExplorationResponse:
            print(response.error_message)
            assert True == False
        else:
            assert response.id == _EXPLORATION_1_ID
    ```

4. Get an exploration, by ID:

    ```python
    from mindleap_starter_python_client.exploration_service import *
    from mindleap_starter_python_client.services import ResponseStatus
    
    exploration_service: ExplorationService = ExplorationService()
    
    _EXPLORATION_1_ID: UUID = UUID("00000000-0000-0000-0000-000000000001")
    
    def test_get_exploration_by_id() -> None:
        response: Exploration | ExplorationResponse = exploration_service.get_exploration_by_id(_EXPLORATION_1_ID)
        if type(response) is ExplorationResponse:
            print(response.error_message)
            assert True == False
        else:
            assert response.id == _EXPLORATION_1_ID
    ```

5. Delete an exploration:

    ```python
    from mindleap_starter_python_client.exploration_service import *
    from mindleap_starter_python_client.services import ResponseStatus
    
    exploration_service: ExplorationService = ExplorationService()
    
    _EXPLORATION_1_ID: UUID = UUID("00000000-0000-0000-0000-000000000001")
    
    def test_delete_exploration() -> None:
        response: GenericResponse = exploration_service.delete_exploration(_EXPLORATION_1_ID)
        assert response.status == ResponseStatus.SUCCESS
    ```

from mindleap_starter_python_client.graph_model_service import *
from mindleap_starter_python_client.services import ResponseStatus

graph_model_service: GraphModelService = GraphModelService()

_SIMPLE_MODEL_ID: UUID = UUID("00000000-0000-0000-0000-000000000001")
_SIMPLE_MODEL_NAME: str = "Simple Model"
_COMPLEX_MODEL_ID: UUID = UUID("00000000-0000-0000-0000-000000000002")
_COMPLEX_MODEL_NAME: str = "Complex Model"

def test_delete_all() -> None:
    graph_models: list[GraphModel] = graph_model_service.get_graph_models()
    for graph_model in graph_models:
        graph_model_service.delete_graph_model(graph_model.id)

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

def test_get_all_graph_models() -> None:
    response: list[GraphModel] | GraphModelsResponse = graph_model_service.get_graph_models()
    if type(response) is GraphModelsResponse:
        print(response.error_message)
        assert True == False
    else:
        assert len(response) > 0

def test_get_graph_model_by_name() -> None:
    response: GraphModel | GraphModelResponse = graph_model_service.get_graph_model_by_name(_SIMPLE_MODEL_NAME)
    if type(response) is GraphModelResponse:
        print(response.error_message)
        assert True == False
    else:
        assert response.id == _SIMPLE_MODEL_ID

def test_get_graph_model_by_id() -> None:
    response: GraphModel | GraphModelResponse = graph_model_service.get_graph_model_by_id(_SIMPLE_MODEL_ID)
    if type(response) is GraphModelResponse:
        print(response.error_message)
        assert True == False
    else:
        assert response.id == _SIMPLE_MODEL_ID

def test_delete_graph_model() -> None:
    response: GenericResponse = graph_model_service.delete_graph_model(_SIMPLE_MODEL_ID)
    assert response.status == ResponseStatus.SUCCESS

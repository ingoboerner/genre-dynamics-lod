"""SKOS

see also https://www.w3.org/TR/2009/REC-skos-reference-20090818/

"""

from rdflib import Namespace
from .entity import Entity

NAMESPACE = "http://www.w3.org/2004/02/skos/core#"

SKOS = Namespace(NAMESPACE)


class SkosConcept(Entity):
    """skos:Concept

    skos:prefLabel Literal
    skos:altLabel Literal
    skos:hiddenLabel Literal
    skos:broader skos:Concept
    skos:narrower skos:Concept
    skos:related skos:Concept
    skos:note
    skos:scopeNote
    skos:example
    skos:historyNote
    skos:editorialNote
    skos:changeNote

    skos:broadMatch
    skos:relatedMatch
    skos:exactMatch
    """
    class_uri = NAMESPACE + "Concept"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def skos_pref_label(self, content: str, lang: str = None) -> bool:
        """skos:prefLabel: Literal

        Args:
            content (str): Textual content
            lang (str, optional): Language of the content. Added to the Literal.

        Returns:
             bool: True if added
        """
        prop = SKOS.prefLabel

        return self.add_property_to_literal_value_triple(content, prop=prop, lang=lang)

    def skos_alt_label(self, content: str, lang: str = None) -> bool:
        """skos:altLabel: Literal

        Args:
            content (str): Textual content
            lang (str, optional): Language of the content. Added to the Literal.

        Returns:
             bool: True if added
        """
        prop = SKOS.altLabel

        return self.add_property_to_literal_value_triple(content, prop=prop, lang=lang)

    def skos_hidden_label(self, content: str, lang: str = None) -> bool:
        """skos:hiddenLabel: Literal

        Args:
            content (str): Textual content
            lang (str, optional): Language of the content. Added to the Literal.

        Returns:
             bool: True if added
        """
        prop = SKOS.hiddenLabel

        return self.add_property_to_literal_value_triple(content, prop=prop, lang=lang)

    def skos_broader(self, *entities, uris: list = None) -> bool:
        """skos:broader (skos:narrower): skos:Concept

        Add triples "skos:broader" and inverse to the self.graph either for each passed entity
        or for each URI provided in "uris".

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
            bool: True if added

        """
        prop = SKOS.broader
        prop_inverse = SKOS.narrower

        range_class_constraint = SkosConcept

        return self.add_triples(entities=list(entities),
                                uris=uris,
                                prop=prop,
                                prop_inverse=prop_inverse,
                                range_class_constraint=range_class_constraint)

    def skos_narrower(self, *entities, uris: list = None) -> bool:
        """skos:narrower (skos:braoder): skos:Concept

        Add triples "skos:narrower" and inverse to the self.graph either for each passed entity
        or for each URI provided in "uris".

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
            bool: True if added

        """
        prop = SKOS.narrower
        prop_inverse = SKOS.broader

        range_class_constraint = SkosConcept

        return self.add_triples(entities=list(entities),
                                uris=uris,
                                prop=prop,
                                prop_inverse=prop_inverse,
                                range_class_constraint=range_class_constraint)

    def skos_related(self, *entities, uris: list = None) -> bool:
        """skos:related: skos:Concept

        Add triples "skos:related" and inverse to the self.graph either for each passed entity
        or for each URI provided in "uris".

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
            bool: True if added

        """
        prop = SKOS.related
        prop_inverse = SKOS.related

        range_class_constraint = SkosConcept

        return self.add_triples(entities=list(entities),
                                uris=uris,
                                prop=prop,
                                prop_inverse=prop_inverse,
                                range_class_constraint=range_class_constraint)

    def skos_note(self, content: str, lang: str = None) -> bool:
        """skos:note: Literal

        Args:
            content (str): Textual content
            lang (str, optional): Language of the content. Added to the Literal.

        Returns:
             bool: True if added
        """
        prop = SKOS.note

        return self.add_property_to_literal_value_triple(content, prop=prop, lang=lang)

    def skos_scope_note(self, content: str, lang: str = None) -> bool:
        """skos:scopeNote: Literal

        Args:
            content (str): Textual content
            lang (str, optional): Language of the content. Added to the Literal.

        Returns:
             bool: True if added
        """
        prop = SKOS.scopeNote

        return self.add_property_to_literal_value_triple(content, prop=prop, lang=lang)

    def skos_example(self, content: str, lang: str = None) -> bool:
        """skos:example: Literal

        Args:
            content (str): Textual content
            lang (str, optional): Language of the content. Added to the Literal.

        Returns:
             bool: True if added
        """
        prop = SKOS.example

        return self.add_property_to_literal_value_triple(content, prop=prop, lang=lang)

    def skos_history_note(self, content: str, lang: str = None) -> bool:
        """skos:historyNote: Literal

        Args:
            content (str): Textual content
            lang (str, optional): Language of the content. Added to the Literal.

        Returns:
             bool: True if added
        """
        prop = SKOS.historyNote

        return self.add_property_to_literal_value_triple(content, prop=prop, lang=lang)

    def skos_editorial_note(self, content: str, lang: str = None) -> bool:
        """skos:editorialNote: Literal

        Args:
            content (str): Textual content
            lang (str, optional): Language of the content. Added to the Literal.

        Returns:
             bool: True if added
        """
        prop = SKOS.editorialNote

        return self.add_property_to_literal_value_triple(content, prop=prop, lang=lang)

    def skos_change_note(self, content: str, lang: str = None) -> bool:
        """skos:changeNote: Literal

        Args:
            content (str): Textual content
            lang (str, optional): Language of the content. Added to the Literal.

        Returns:
             bool: True if added
        """
        prop = SKOS.changeNote

        return self.add_property_to_literal_value_triple(content, prop=prop, lang=lang)

    def skos_in_scheme(self, *entities, uris: list = None) -> bool:
        """skos:inScheme: skos:ConceptScheme

        Add triples "skos:inScheme" to the self.graph either for each passed entity
        or for each URI provided in "uris".

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
            bool: True if added

        """
        prop = SKOS.inScheme

        range_class_constraint = SkosConceptScheme

        return self.add_triples(entities=list(entities),
                                uris=uris,
                                prop=prop,
                                range_class_constraint=range_class_constraint)

    def skos_broad_match(self, *entities, uris: list = None) -> bool:
        """skos:broadMatch: skos:Concept

        Add triples "skos:broadMatch" to the self.graph either for each passed entity
        or for each URI provided in "uris".

        TODO: check if inverse

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
            bool: True if added

        """
        prop = SKOS.broadMatch
        # Not sure about the inverse; if it can be assumed automatically
        # prop_inverse = SKOS.narrowMatch

        range_class_constraint = SkosConcept

        return self.add_triples(entities=list(entities),
                                uris=uris,
                                prop=prop,
                                #prop_inverse=prop_inverse,
                                range_class_constraint=range_class_constraint)

    def skos_narrow_match(self, *entities, uris: list = None) -> bool:
        """skos:narrowMatch: skos:Concept

        Add triples "skos:narrowMatch" to the self.graph either for each passed entity
        or for each URI provided in "uris".

        TODO: check if inverse

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
            bool: True if added

        """
        prop = SKOS.narrowMatch
        # Not sure about the inverse; if it can be assumed automatically
        # prop_inverse = SKOS.broadMatch

        range_class_constraint = SkosConcept

        return self.add_triples(entities=list(entities),
                                uris=uris,
                                prop=prop,
                                # prop_inverse=prop_inverse,
                                range_class_constraint=range_class_constraint)

    def skos_related_match(self, *entities, uris: list = None) -> bool:
        """skos:relatedMatch: skos:Concept

        Add triples "skos:relatedMatch" to the self.graph either for each passed entity
        or for each URI provided in "uris".

        TODO: check if inverse

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
            bool: True if added

        """
        prop = SKOS.relatedMatch
        # Not sure about the inverse; if it can be assumed automatically
        # prop_inverse = SKOS.relatedMatch

        range_class_constraint = SkosConcept

        return self.add_triples(entities=list(entities),
                                uris=uris,
                                prop=prop,
                                # prop_inverse=prop_inverse,
                                range_class_constraint=range_class_constraint)

    def skos_exact_match(self, *entities, uris: list = None) -> bool:
        """skos:exactMatch: skos:Concept

        Add triples "skos:exactMatch" to the self.graph either for each passed entity
        or for each URI provided in "uris".

        TODO: check if inverse

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
            bool: True if added

        """
        prop = SKOS.exactMatch
        # Not sure about the inverse; if it can be assumed automatically
        # prop_inverse = SKOS.exactMatch

        range_class_constraint = SkosConcept

        return self.add_triples(entities=list(entities),
                                uris=uris,
                                prop=prop,
                                # prop_inverse=prop_inverse,
                                range_class_constraint=range_class_constraint)


class SkosConceptScheme(Entity):
    """skos:ConceptScheme

    skos:hasTopConcept

    """
    class_uri = NAMESPACE + "ConceptScheme"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def skos_has_top_concept(self, *entities, uris: list = None) -> bool:
        """skos:hasTopConcept: skos:Concept

        Add triples "skos:hasTopConcept" and inverse (skos:inScheme) to the self.graph either for each passed entity
        or for each URI provided in "uris".

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
            bool: True if added

        """
        prop = SKOS.hasTopConcept
        prop_inverse = SKOS.topConceptOf

        range_class_constraint = SkosConcept

        return self.add_triples(entities=list(entities),
                                uris=uris,
                                prop=prop,
                                prop_inverse=prop_inverse,
                                range_class_constraint=range_class_constraint)
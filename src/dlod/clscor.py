"""CLSCor

Utility classes for CLSCor data generation
"""

from rdflib import Namespace
from .skos import SkosConcept, SkosConceptScheme
from .cidoc import E55Type, E32AuthorityDocument
from .crmcls import X7Format, X3Feature
from .ontologies import SKOSNAMESPACE, CIDOCNAMESPACE

SKOS = Namespace(SKOSNAMESPACE)
CRM = Namespace(CIDOCNAMESPACE)


class CLSCorVocabTerm(E55Type, SkosConcept):
    """Vocabulary Term

    Vocabulary Term is an instance of SkosConcept AND E55 Type
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # multiple instantiation is needed here
        self.graph = self.graph + self.instance_of_class(class_uri=SkosConcept.class_uri)
        self.graph = self.graph + self.instance_of_class(class_uri=E55Type.class_uri)

    def is_term_in(self, *entities, uris: list = None, skos_top_concept: bool = False) -> bool:
        """is term in

        Connects a vocabulary term 'CLSCorVocabTerm' to a vocabulary 'CLSCorVocab'.
        This results in
        - skos:Concept skos:inScheme CLSCorVocab
        - if it is a top concept (flag: 'skos_top_concept' the property skos:topConcept will be added)
        - crm:E55_Type crm:P71i_is_listed_in crm:E32_Authority_Document
        - crm:E32_Authority_Document crm:P71_lists crm:E55_Type


        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this
            skos_top_concept (bool, optional): Indicates if a vocab term is a top concept of a skos:ConceptScheme.
                Defaults to False.

        Returns:
            bool: True if added

        """

        prop = CRM.P71i_is_listed_in
        prop_inverse = CRM.P71_lists

        range_class_constraint = E32AuthorityDocument

        self.add_triples(entities=list(entities),
                         uris=uris,
                         prop=prop,
                         prop_inverse=prop_inverse,
                         range_class_constraint=range_class_constraint)

        prop = SKOS.inScheme
        if skos_top_concept is True:
            prop_inverse = SKOS.topConcept

        range_class_constraint = SkosConceptScheme

        self.add_triples(entities=list(entities),
                         uris=uris,
                         prop=prop,
                         prop_inverse=prop_inverse,
                         range_class_constraint=range_class_constraint)

        return True


class CLSCorVocab(E32AuthorityDocument, SkosConceptScheme):
    """Vocabulary Term

    Vocabulary Term is an instance of SkosConcept AND E55 Type
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # multiple instantiation is needed here
        self.graph = self.graph + self.instance_of_class(class_uri=SkosConceptScheme.class_uri)
        self.graph = self.graph + self.instance_of_class(class_uri=E32AuthorityDocument.class_uri)


class CLSCorFormat(CLSCorVocabTerm, X7Format):
    """Format

    Format is an instance of cls:X7Format, crm:E55 Type (because of PE43EncodingType subClass E55) and skos:Concept
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # multiple instantiation is needed here
        self.graph = self.graph + self.instance_of_class(class_uri=SkosConcept.class_uri)
        self.graph = self.graph + self.instance_of_class(class_uri=X7Format.class_uri)


class CLSCorFeature(CLSCorVocabTerm, X3Feature):
    """Feature

    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # multiple instantiation is needed here
        self.graph = self.graph + self.instance_of_class(class_uri=SkosConcept.class_uri)
        self.graph = self.graph + self.instance_of_class(class_uri=X3Feature.class_uri)




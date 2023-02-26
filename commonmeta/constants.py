"""Constants for commonmeta-py"""
from typing import Optional, TypedDict, List


class Commonmeta(TypedDict):
    """TypedDict for Commonmeta"""

    id: str
    type: str
    doi: str
    url: str
    creators: List[dict]
    titles: List[dict]
    publisher: str
    publication_year: int
    additional_type: Optional[str]
    subjects: Optional[List[dict]]
    contributors: Optional[List[dict]]
    dates: Optional[List[dict]]
    language: Optional[str]
    alternate_identifiers: Optional[List[dict]]
    sizes: Optional[List[dict]]
    formats: Optional[List[dict]]
    version: Optional[str]
    rights: Optional[List[dict]]
    descriptions: Optional[List[dict]]
    geo_locations: Optional[List[dict]]
    funding_references: Optional[List[dict]]
    references: Optional[List[dict]]
    container: Optional[dict]
    date_created: Optional[str]
    date_registered: Optional[str]
    date_published: Optional[str]
    date_updated: Optional[str]
    content_url: Optional[List[dict]]
    agency: Optional[str]
    state: str
    schema_version: Optional[str]


# source: https://www.bibtex.com/e/entry-types/
BIB_TO_CM_TRANSLATIONS = {
    "article": "JournalArticle",
    "book": "Book",
    "booklet": "Book",
    "inbook": "BookChapter",
    "inproceedings": "ProceedingsArticle",
    "manual": "Report",
    "mastersthesis": "Dissertation",
    "misc": "Other",
    "phdthesis": "Dissertation",
    "proceedings": "Proceedings",
    "techreport": "Report",
    "unpublished": "Manuscript",
}

CM_TO_BIB_TRANSLATIONS = {
    "Article": "article",
    "Book": "book",
    "BookChapter": "inbook",
    "Dissertation": "phdthesis",
    "JournalArticle": "article",
    "Manuscript": "unpublished",
    "Other": "misc",
    "Proceedings": "proceedings",
    "ProceedingsArticle": "inproceedings",
    "Report": "techreport",
}
    
# source: https://docs.citationstyles.org/en/stable/specification.html?highlight=book#appendix-iii-types
CP_TO_CM_TRANSLATIONS = {
    "article": "Article",
    "article-journal": "JournalArticle",
    "article-magazine": "Article",
    "article-newspaper": "Article",
    "bill": "LegalDocument",
    "book": "Book",
    "broadcast": "Audiovisual",
    "chapter": "BookChapter",
    "classic": "Book",
    "collection": "Collection",
    "dataset": "Dataset",
    "document": "Document",
    "entry": "Entry",
    "entry-dictionary": "Entry",
    "entry-encyclopedia": "Entry",
    "event": "Event",
    "figure": "Figure",
    "graphic": "Image",
    "hearing": "LegalDocument",
    "interview": "Document",
    "legal_case": "LegalDocument",
    "legislation": "LegalDocument",
    "manuscript": "Manuscript",
    "map": "Map",
    "motion_picture": "Audiovisual",
    "musical_score": "Document",
    "pamphlet": "Document",
    "paper-conference": "ProceedingsArticle",
    "patent": "Patent",
    "performance": "Performance",
    "periodical": "Journal",
    "personal_communication": "PersonalCommunication",
    "post": "Post",
    "post-weblog": "Article",
    "regulation": "LegalDocument",
    "report": "Report",
    "review": "Review",
    "review-book": "Review",
    "software": "Software",
    "song": "Audiovisual",
    "speech": "Speech",
    "standard": "Standard",
    "thesis": "Dissertation",
    "treaty": "LegalDocument",
    "webpage": "WebPage",
}

CM_TO_CP_TRANSLATIONS = {
    "Article": "article",
    "JournalArticle": "article-journal",
    "Book": "book",
    "BookChapter": "chapter",
    "Collection": "collection",
    "Dataset": "dataset",
    "Document": "document",
    "Entry": "entry",
    "Event": "event",
    "Figure": "figure",
    "Image": "graphic",
    "LegalDocument": "legal_case",
    "Manuscript": "manuscript",
    "Map": "map",
    "Audiovisual": "motion_picture",
    "Patent": "patent",
    "Performance": "performance",
    "Journal": "periodical",
    "PersonalCommunication": "personal_communication",
    "Post": "post",
    "Report": "report",
    "Review": "review",
    "Software": "software",
    "Speech": "speech",
    "Standard": "standard",
    "Dissertation": "thesis",
    "WebPage": "webpage",
}

# source: http://api.crossref.org/types
CR_TO_CM_TRANSLATIONS = {
    "BookChapter": "BookChapter",
    "BookPart": "BookPart",
    "BookSection": "BookSection",
    "BookSeries": "BookSeries",
    "BookSet": "BookSet",
    "BookTrack": "BookTrack",
    "Book": "Book",
    "Component": "Component",
    "Database": "Database",
    "Dataset": "Dataset",
    "Dissertation": "Dissertation",
    "EditedBook": "EditedBook",
    "Grant": "Grant",
    "JournalArticle": "JournalArticle",
    "JournalIssue": "JournalIssue",
    "JournalVolume": "JournalVolume",
    "Journal": "Journal",
    "Monograph": "Book",
    "Other": "Other",
    "PeerReview": "Review",
    "PostedContent": "Article",
    "ProceedingsArticle": "ProceedingsArticle",
    "ProceedingsSeries": "ProceedingsSeries",
    "Proceedings": "Proceedings",
    "ReferenceBook": "ReferenceBook",
    "ReferenceEntry": "Entry",
    "ReportComponent": "ReportComponent",
    "ReportSeries": "ReportSeries",
    "Report": "Report",
    "Standard": "Standard",
}

CM_TO_CR_TRANSLATIONS = {
    "Article": "PostedContent",
    "BookChapter": "BookChapter",
    "BookPart": "BookPart",
    "BookSection": "BookSection",
    "BookSeries": "BookSeries",
    "BookSet": "BookSet",
    "BookTrack": "BookTrack",
    "Book": "Book",
    "Component": "Component",
    "Database": "Database",
    "Dataset": "Dataset",
    "Dissertation": "Dissertation",
    "EditedBook": "EditedBook",
    "JournalArticle": "JournalArticle",
    "Other": "Other",
    "Review": "PeerReview",
}

# source: https://github.com/datacite/schema/blob/master/source/meta/kernel-4/include/datacite-resourceType-v4.xsd
DC_TO_CM_TRANSLATIONS = {
    "Audiovisual": "Audiovisual",
    "BlogPosting": "Article",
    "Book": "Book",
    "BookChapter": "BookChapter",
    "Collection": "Collection",
    "ComputationalNotebook": "ComputationalNotebook",
    "ConferencePaper": "ProceedingsArticle",
    "ConferenceProceeding": "Proceedings",
    "DataPaper": "JournalArticle",
    "Dataset": "Dataset",
    "Dissertation": "Dissertation",
    "Event": "Event",
    "Image": "Image",
    "InteractiveResource": "InteractiveResource",
    "Journal": "Journal",
    "JournalArticle": "JournalArticle",
    "Model": "Model",
    "OutputManagementPlan": "OutputManagementPlan",
    "PeerReview": "PeerReview",
    "PhysicalObject": "PhysicalObject",
    "Poster": "Speech",
    "Preprint": "Article",
    "Report": "Report",
    "Service": "Service",
    "Software": "Software",
    "Sound": "Sound",
    "Standard": "Standard",
    "Text": "Document",
    "Thesis": "Dissertation",
    "Workflow": "Workflow",
    "Other": "Other",
}

CM_TO_DC_TRANSLATIONS = {
    "Article": "Preprint",
    "Audiovisual": "Audiovisual",
    "Book": "Book",
    "BookChapter": "BookChapter",
    "Collection": "Collection",
    "Dataset": "Dataset",
    "Document": "Text",
    "Entry": "Text",
    "Event": "Event",
    "Figure": "Image",
    "Image": "Image",
    "JournalArticle": "JournalArticle",
    "LegalDocument": "Text",
    "Manuscript": "Text",
    "Map": "Image",
    "Patent": "Text",
    "Performance": "Audiovisual",
    "PersonalCommunication": "Text",
    "Post": "Text",
    "ProceedingsArticle": "ConferencePaper",
    "Proceedings": "ConferenceProceeding",
    "Report": "Report",
    "Review": "PeerReview",
    "Software": "Software",
    "Sound": "Sound",
    "Standard": "Standard",
    "WebPage": "Text",
}

RIS_TO_CM_TRANSLATIONS = {
    "ABST": "Text",
    "ADVS": "Text",
    "AGGR": "Text",
    "ANCIENT": "Text",
    "ART": "Text",
    "BILL": "Text",
    "BLOG": "Text",
    "BOOK": "Book",
    "CASE": "Text",
    "CHAP": "BookChapter",
    "CHART": "Text",
    "CLSWK": "Text",
    "CTLG": "Collection",
    "COMP": "Software",
    "DATA": "Dataset",
    "DBASE": "Database",
    "DICT": "Dictionary",
    "EBOOK": "Book",
    "ECHAP": "BookChapter",
    "EDBOOK": "Book",
    "EJOUR": "JournalArticle",
    "ELEC": "Text",
    "ENCYC": "Encyclopedia",
    "EQUA": "Equation",
    "FIGURE": "Image",
    "GEN": "CreativeWork",
    "GOVDOC": "GovernmentDocument",
    "GRANT": "Grant",
    "HEAR": "Hearing",
    "ICOMM": "Text",
    "INPR": "Text",
    "JFULL": "JournalArticle",
    "JOUR": "JournalArticle",
    "LEGAL": "LegalRuleOrRegulation",
    "MANSCPT": "Text",
    "MAP": "Map",
    "MGZN": "MagazineArticle",
    "MPCT": "Audiovisual",
    "MULTI": "Audiovisual",
    "MUSIC": "MusicScore",
    "NEWS": "NewspaperArticle",
    "PAMP": "Pamphlet",
    "PAT": "Patent",
    "PCOMM": "PersonalCommunication",
    "RPRT": "Report",
    "SER": "SerialPublication",
    "SLIDE": "Slide",
    "SOUND": "SoundRecording",
    "STAND": "Standard",
    "THES": "Dissertation",
    "UNBILL": "UnenactedBill",
    "UNPB": "UnpublishedWork",
    "VIDEO": "Audiovisual",
    "WEB": "WebPage",
}

CM_TO_RIS_TRANSLATIONS = {
    "Article": "JOUR",
    "Audiovisual": "VIDEO",
    "Book": "BOOK",
    "BookChapter": "CHAP",
    "Collection": "CTLG",
    "Dataset": "DATA",
    "Document": "GEN",
    "Entry": "DICT",
    "Event": "GEN",
    "Figure": "FIGURE",
    "Image": "FIGURE",
    "JournalArticle": "JOUR",
    "LegalDocument": "GEN",
    "Manuscript": "GEN",
    "Map": "MAP",
    "Patent": "PAT",
    "Performance": "GEN",
    "PersonalCommunication": "PCOMM",
    "Post": "GEN",
    "ProceedingsArticle": "CPAPER",
    "Proceedings": "CONF",
    "Report": "RPRT",
    "Review": "GEN",
    "Software": "COMP",
    "Sound": "SOUND",
    "Standard": "STAND",
    "WebPage": "WEB",
}

SO_TO_CM_TRANSLATIONS = {
    "Article": "Article",
    "BlogPosting": "Article",
    "Book": "Book",
    "BookChapter": "BookChapter",
    "CreativeWork": "Other",
    "Dataset": "Dataset",
    "Dissertation": "Dissertation",
    "NewsArticle": "Article",
    "Legislation": "LegalDocument",
    "ScholarlyArticle": "JournalArticle",
    "SoftwareSourceCode": "Software",
}

CM_TO_SO_TRANSLATIONS = {
    "Article": "Article",
    "Book": "Book",
    "BookChapter": "BookChapter",
    "Dataset": "Dataset",
    "Dissertation": "Dissertation",
    "LegalDocument": "Legislation",
    "JournalArticle": "ScholarlyArticle",
    "Software": "SoftwareSourceCode",
}

CR_TO_BIB_TRANSLATIONS = {
    "Proceedings": "proceedings",
    "ReferenceBook": "book",
    "JournalIssue": None,
    "ProceedingsArticle": "inproceedings",
    "Other": None,
    "Dissertation": "phdthesis",
    "Dataset": None,
    "EditedBook": "book",
    "JournalArticle": "article",
    "Journal": None,
    "Report": "techreport",
    "BookSeries": None,
    "ReportSeries": None,
    "BookTrack": None,
    "Standard": None,
    "BookSection": "inbook",
    "BookPart": None,
    "Book": "book",
    "BookChapter": "inbook",
    "StandardSeries": None,
    "Monograph": "book",
    "Component": None,
    "ReferenceEntry": None,
    "JournalVolume": None,
    "BookSet": None,
    "PostedContent": "article",
}

CR_TO_CP_TRANSLATIONS = {
    "Proceedings": None,
    "ReferenceBook": None,
    "JournalIssue": "article-journal",
    "ProceedingsArticle": "paper-conference",
    "Other": None,
    "Dissertation": "thesis",
    "Dataset": "dataset",
    "EditedBook": "book",
    "PostedContent": "article-journal",
    "JournalArticle": "article-journal",
    "Journal": None,
    "Report": "report",
    "BookSeries": None,
    "ReportSeries": None,
    "BookTrack": None,
    "Standard": None,
    "BookSection": "chapter",
    "BookPart": None,
    "Book": "book",
    "BookChapter": "chapter",
    "StandardSeries": None,
    "Monograph": "book",
    "Component": None,
    "ReferenceEntry": "entry-dictionary",
    "JournalVolume": None,
    "BookSet": None,
}

CR_TO_DC_TRANSLATIONS = {
    "Proceedings": None,
    "ReferenceBook": None,
    "JournalIssue": "Text",
    "ProceedingsArticle": "ConferencePaper",
    "Other": "Other",
    "Dissertation": "Dissertation",
    "Dataset": "Dataset",
    "EditedBook": "Book",
    "JournalArticle": "JournalArticle",
    "Journal": "Journal",
    "Report": "Report",
    "BookSeries": None,
    "ReportSeries": None,
    "BookTrack": None,
    "Standard": "Standard",
    "BookSection": "BookChapter",
    "BookPart": None,
    "Book": "Book",
    "BookChapter": "BookChapter",
    "SaComponent": "Text",
    "StandardSeries": "Standard",
    "Monograph": "Book",
    "Component": None,
    "ReferenceEntry": None,
    "JournalVolume": None,
    "BookSet": None,
    "PostedContent": "Preprint",
    "PeerReview": "PeerReview",
}

CR_TO_RIS_TRANSLATIONS = {
    "Proceedings": "CONF",
    "PostedContent": "JOUR",
    "ReferenceBook": "BOOK",
    "JournalIssue": "JOUR",
    "ProceedingsArticle": "CPAPER",
    "Other": "GEN",
    "Dissertation": "THES",
    "Dataset": "DATA",
    "EditedBook": "BOOK",
    "JournalArticle": "JOUR",
    "Journal": None,
    "Report": "RPRT",
    "BookSeries": None,
    "ReportSeries": None,
    "BookTrack": None,
    "Standard": "STAND",
    "BookSection": "CHAP",
    "BookPart": "CHAP",
    "Book": "BOOK",
    "BookChapter": "CHAP",
    "StandardSeries": None,
    "Monograph": "BOOK",
    "Component": None,
    "ReferenceEntry": "DICT",
    "JournalVolume": None,
    "BookSet": None,
}

CR_TO_SO_TRANSLATIONS = {
    "Proceedings": None,
    "ReferenceBook": "Book",
    "JournalIssue": "PublicationIssue",
    "ProceedingsArticle": None,
    "Other": "CreativeWork",
    "Dissertation": "Thesis",
    "Dataset": "Dataset",
    "EditedBook": "Book",
    "JournalArticle": "ScholarlyArticle",
    "Journal": None,
    "Report": "Report",
    "BookSeries": None,
    "ReportSeries": None,
    "BookTrack": None,
    "Standard": None,
    "BookSection": None,
    "BookPart": None,
    "Book": "Book",
    "BookChapter": "Chapter",
    "StandardSeries": None,
    "Monograph": "Book",
    "Component": "CreativeWork",
    "ReferenceEntry": None,
    "JournalVolume": "PublicationVolume",
    "BookSet": None,
    "PostedContent": "ScholarlyArticle",
    "PeerReview": "Review",
}

DC_TO_RIS_TRANSLATIONS = {
    "Audiovisual": "MPCT",
    "Book": "BOOK",
    "BookChapter": "CHAP",
    "Collection": None,
    "ComputationalNotebook": "COMP",
    "ConferencePaper": "CPAPER",
    "ConferenceProceeding": "CONF",
    "DataPaper": None,
    "Dataset": "DATA",
    "Dissertation": "THES",
    "Event": None,
    "Image": "FIGURE",
    "InteractiveResource": None,
    "Journal": None,
    "JournalArticle": "JOUR",
    "Model": None,
    "OutputManagementPlan": None,
    "PeerReview": None,
    "PhysicalObject": None,
    "Preprint": "RPRT",
    "Report": "RRPT",
    "Service": None,
    "Software": "COMP",
    "Sound": "SOUND",
    "Standard": None,
    "Text": "RPRT",
    "Workflow": None,
    "Other": None,
}

DC_TO_SO_TRANSLATIONS = {
    "Audiovisual": "MediaObject",
    "Book": "Book",
    "BookChapter": "Chapter",
    "Collection": "Collection",
    "ComputationalNotebook": "SoftwareSourceCode",
    "ConferencePaper": "Article",
    "ConferenceProceeding": "Periodical",
    "DataPaper": "Article",
    "Dataset": "Dataset",
    "Dissertation": "Thesis",
    "Event": "Event",
    "Image": "ImageObject",
    "InteractiveResource": None,
    "Journal": "Periodical",
    "JournalArticle": "ScholarlyArticle",
    "Model": None,
    "OutputManagementPlan": None,
    "PeerReview": "Review",
    "PhysicalObject": None,
    "Preprint": None,
    "Report": "Report",
    "Service": "Service",
    "Software": "SoftwareSourceCode",
    "Sound": "AudioObject",
    "Standard": None,
    "Text": "ScholarlyArticle",
    "Workflow": None,
    "Other": "CreativeWork",
    # not part of DataCite schema, but used internally
    "Periodical": "Periodical",
    "DataCatalog": "DataCatalog",
}

RIS_TO_BIB_TRANSLATIONS = {
    "JOUR": "article",
    "BOOK": "book",
    "CHAP": "inbook",
    "CPAPER": "inproceedings",
    "GEN": "misc",
    "THES": "phdthesis",
    "CONF": "proceedings",
    "RPRT": "techreport",
    "UNPD": "unpublished",
}

RIS_TO_CP_TRANSLATIONS = {"JOUR": "article-journal"}

RIS_TO_DC_TRANSLATIONS = {
    "BLOG": "Text",
    "GEN": "Text",
    "CTLG": "Collection",
    "DATA": "Dataset",
    "FIGURE": "Image",
    "THES": "Dissertation",
    "MPCT": "Audiovisual",
    "JOUR": "JournalArticle",
    "COMP": "Software",
    "VIDEO": "Audiovisual",
    "ELEC": "Text",
}

RIS_TO_SO_TRANSLATIONS = {
    "BLOG": "BlogPosting",
    "GEN": "CreativeWork",
    "CTLG": "DataCatalog",
    "DATA": "Dataset",
    "FIGURE": "ImageObject",
    "THES": "Thesis",
    "MPCT": "Movie",
    "JOUR": "ScholarlyArticle",
    "COMP": "SoftwareSourceCode",
    "VIDEO": "VideoObject",
    "ELEC": "WebPage",
}

SO_TO_BIB_TRANSLATIONS = {
    "Article": "article",
    "AudioObject": "misc",
    "Thesis": "phdthesis",
    "Blog": "misc",
    "BlogPosting": "article",
    "Collection": "misc",
    "CreativeWork": "misc",
    "DataCatalog": "misc",
    "Dataset": "misc",
    "Event": "misc",
    "ImageObject": "misc",
    "Movie": "misc",
    "PublicationIssue": "misc",
    "ScholarlyArticle": "article",
    "Service": "misc",
    "SoftwareSourceCode": "misc",
    "VideoObject": "misc",
    "WebPage": "misc",
    "WebSite": "misc",
}

SO_TO_CP_TRANSLATIONS = {
    "Article": "article-newspaper",
    "AudioObject": "song",
    "Blog": "report",
    "BlogPosting": "post-weblog",
    "Collection": None,
    "CreativeWork": None,
    "DataCatalog": "dataset",
    "Dataset": "dataset",
    "Event": None,
    "ImageObject": "graphic",
    "Movie": "motion_picture",
    "PublicationIssue": None,
    "Report": "report",
    "ScholarlyArticle": "article-journal",
    "Service": None,
    "Thesis": "thesis",
    "VideoObject": "broadcast",
    "WebPage": "webpage",
    "WebSite": "webpage",
}

SO_TO_DC_TRANSLATIONS = {
    "Article": "Preprint",
    "AudioObject": "Sound",
    "Blog": "Text",
    "BlogPosting": "Preprint",
    "Book": "Book",
    "Chapter": "BookChapter",
    "Collection": "Collection",
    "CreativeWork": "Text",
    "DataCatalog": "Dataset",
    "Dataset": "Dataset",
    "Event": "Event",
    "ImageObject": "Image",
    "Movie": "Audiovisual",
    "PublicationIssue": "Text",
    "Report": "Report",
    "ScholarlyArticle": "Text",
    "Thesis": "Text",
    "Service": "Service",
    "Review": "PeerReview",
    "SoftwareSourceCode": "Software",
    "VideoObject": "Audiovisual",
    "WebPage": "Text",
    "WebSite": "Text",
}

SO_TO_DC_RELATION_TYPES = {
    "citation": "References",
    "isBasedOn": "IsSupplementedBy",
    "sameAs": "IsIdenticalTo",
    "isPartOf": "IsPartOf",
    "hasPart": "HasPart",
    "isPredecessor": "IsPreviousVersionOf",
    "isSuccessor": "IsNewVersionOf",
}

SO_TO_DC_REVERSE_RELATION_TYPES = {
    "citation": "IsReferencedBy",
    "isBasedOn": "IsSupplementTo",
    "sameAs": "IsIdenticalTo",
    "isPartOf": "HasPart",
    "hasPart": "IsPartOf",
    "isPredecessor": "IsNewVersionOf",
    "isSuccessor": "IsPreviousVersionOf",
}

SO_TO_RIS_TRANSLATIONS = {
    "Article": "GEN",
    "AudioObject": None,
    "Blog": None,
    "BlogPosting": "BLOG",
    "Collection": None,
    "CreativeWork": "GEN",
    "DataCatalog": "CTLG",
    "Dataset": "DATA",
    "Event": None,
    "ImageObject": "FIGURE",
    "Movie": "MPCT",
    "Report": "RPRT",
    "PublicationIssue": None,
    "ScholarlyArticle": "JOUR",
    "Service": None,
    "SoftwareSourceCode": "COMP",
    "VideoObject": "VIDEO",
    "WebPage": "ELEC",
    "WebSite": None,
}

CP_TO_SO_TRANSLATIONS = {
    "song": "AudioObject",
    "post-weblog": "BlogPosting",
    "dataset": "Dataset",
    "graphic": "ImageObject",
    "motion_picture": "Movie",
    "article-journal": "ScholarlyArticle",
    "broadcast": "VideoObject",
    "webpage": "WebPage",
}

CP_TO_RIS_TRANSLATIONS = {
    "post-weblog": "BLOG",
    "dataset": "DATA",
    "graphic": "FIGURE",
    "book": "BOOK",
    "motion_picture": "MPCT",
    "article-journal": "JOUR",
    "broadcast": "MPCT",
    "webpage": "ELEC",
}

CP_TO_DC_TRANSLATIONS = {
    "song": "Audiovisual",
    "post-weblog": "Text",
    "dataset": "Dataset",
    "graphic": "Image",
    "motion_picture": "Audiovisual",
    "article-journal": "JournalArticle",
    "broadcast": "Audiovisual",
    "webpage": "Text",
}

CROSSREF_CONTAINER_TYPES = {
    "JournalArticle": "journal",
    "BookChapter": "book",
    "Dataset": "database",
}

"""Constants for commonmeta-py"""

from typing import Optional, TypedDict, List


class Commonmeta(TypedDict):
    """TypedDict for Commonmeta"""

    id: str
    type: str
    url: str
    creators: List[dict]
    titles: List[dict]
    publisher: dict
    date: dict
    additional_type: Optional[str]
    subjects: Optional[List[dict]]
    contributors: Optional[List[dict]]
    language: Optional[str]
    identifiers: Optional[List[dict]]
    relations: Optional[List[dict]]
    sizes: Optional[List[dict]]
    formats: Optional[List[dict]]
    version: Optional[str]
    license: Optional[dict]
    descriptions: Optional[List[dict]]
    geo_locations: Optional[List[dict]]
    funding_references: Optional[List[dict]]
    references: Optional[List[dict]]
    container: Optional[dict]
    files: Optional[List[dict]]
    agency: Optional[str]
    state: str


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
CSL_TO_CM_TRANSLATIONS = {
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
    "speech": "Presentation",
    "standard": "Standard",
    "thesis": "Dissertation",
    "treaty": "LegalDocument",
    "webpage": "WebPage",
}

CM_TO_CSL_TRANSLATIONS = {
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
    "Report": "report",
    "Review": "review",
    "Software": "software",
    "Presentation": "speech",
    "Standard": "standard",
    "Dissertation": "thesis",
    "WebPage": "webpage",
}

# source: http://api.crossref.org/types
CR_TO_CM_TRANSLATIONS = {
    "book-chapter": "BookChapter",
    "book-part": "BookPart",
    "book-section": "BookSection",
    "book-series": "BookSeries",
    "book-set": "BookSet",
    "book-track": "BookTrack",
    "book": "Book",
    "component": "Component",
    "database": "Database",
    "dataset": "Dataset",
    "dissertation": "Dissertation",
    "edited-book": "Book",
    "grant": "Grant",
    "journal-article": "JournalArticle",
    "journal-issue": "JournalIssue",
    "journal-volume": "JournalVolume",
    "journal": "Journal",
    "monograph": "Book",
    "other": "Other",
    "peer-review": "PeerReview",
    "posted-content": "Article",
    "proceedings-article": "ProceedingsArticle",
    "proceedings-series": "ProceedingsSeries",
    "proceedings": "Proceedings",
    "reference-book": "Book",
    "reference-entry": "Entry",
    "report-component": "ReportComponent",
    "report-series": "ReportSeries",
    "report": "Report",
    "standard": "Standard",
}

CM_TO_CR_TRANSLATIONS = {
    "Article": "PostedContent",
    "BookChapter": "BookChapter",
    "BookSeries": "BookSeries",
    "Book": "Book",
    "Component": "Component",
    "Dataset": "Dataset",
    "Dissertation": "Dissertation",
    "Grant": "Grant",
    "JournalArticle": "JournalArticle",
    "JournalIssue": "JournalIssue",
    "JournalVolume": "JournalVolume",
    "Journal": "Journal",
    "ProceedingsArticle": "ProceedingsArticle",
    "ProceedingsSeries": "ProceedingsSeries",
    "Proceedings": "Proceedings",
    "ReportComponent": "ReportComponent",
    "ReportSeries": "ReportSeries",
    "Report": "Report",
    "Review": "PeerReview",
    "Other": "Other",
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
    "Instrument": "Instrument",
    "InteractiveResource": "InteractiveResource",
    "Journal": "Journal",
    "JournalArticle": "JournalArticle",
    "Model": "Model",
    "OutputManagementPlan": "OutputManagementPlan",
    "PeerReview": "PeerReview",
    "PhysicalObject": "PhysicalObject",
    "Poster": "Presentation",
    "Preprint": "Article",
    "Report": "Report",
    "Service": "Service",
    "Software": "Software",
    "Sound": "Sound",
    "Standard": "Standard",
    "StudyRegistration": "StudyRegistration",
    "Text": "Document",
    "Thesis": "Dissertation",
    "Workflow": "Workflow",
    "Other": "Other",
}

# https://github.com/zenodo/zenodo/blob/master/zenodo/modules/records/data/objecttypes.json
INVENIORDM_TO_CM_TRANSLATIONS = {
    "book": "Book",
    "section": "BookChapter",
    "conferencepaper": "ProceedingsArticle",
    "patent": "Patent",
    "publication": "JournalArticle",
    "publication-preprint": "Article",
    "report": "Report",
    "softwaredocumentation": "Software",
    "thesis": "Dissertation",
    "technicalnote": "Report",
    "workingpaper": "Report",
    "datamanagementplan": "OutputManagementPlan",
    "annotationcollection": "Collection",
    "taxonomictreatment": "Collection",
    "peerreview": "PeerReview",
    "poster": "Presentation",
    "presentation": "Presentation",
    "dataset": "Dataset",
    "figure": "Image",
    "plot": "Image",
    "drawing": "Image",
    "photo": "Image",
    "image": "Image",
    "video": "Audiovisual",
    "software": "Software",
    "lesson": "InteractiveResource",
    "physicalobject": "PhysicalObject",
    "workflow": "Workflow",
    "other": "Other",
}

CM_TO_INVENIORDM_TRANSLATIONS = {
    "Article": "publication-preprint",
    "Book": "book",
    "Dataset": "dataset",
    "Image": "image-other",
    "JournalArticle": "publication-article",
    "Presentation": "presentation",
    "Software": "software",
    "Other": "other",
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
    "Instrument": "Instrument",
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
    "StudyRegistration": "StudyRegistration",
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
    "Dissertation": "THES",
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
    "DigitalDocument": "Document",
    "Dissertation": "Dissertation",
    "Instrument": "Instrument",
    "NewsArticle": "Article",
    "Legislation": "LegalDocument",
    "Report": "Report",
    "ScholarlyArticle": "JournalArticle",
    "SoftwareSourceCode": "Software",
}

CM_TO_SO_TRANSLATIONS = {
    "Article": "Article",
    "Audiovisual": "CreativeWork",
    "Book": "Book",
    "BookChapter": "BookChapter",
    "Collection": "CreativeWork",
    "Dataset": "Dataset",
    "Dissertation": "Dissertation",
    "Document": "CreativeWork",
    "Entry": "CreativeWork",
    "Event": "CreativeWork",
    "Figure": "CreativeWork",
    "Image": "CreativeWork",
    "Instrument": "Instrument",
    "JournalArticle": "ScholarlyArticle",
    "LegalDocument": "Legislation",
    "Software": "SoftwareSourceCode",
    "Presentation": "PresentationDigitalDocument",
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

CROSSREF_CONTAINER_TYPES = {
    "book-chapter": "book",
    "dataset": "database",
    "journal-article": "journal",
    "journal-issue": "journal",
    "monograph": "book-series",
    "proceedings-article": "proceedings",
    "posted-content": "periodical",
}

COMMONMETA_CONTAINER_TYPES = {
    "Article": "Periodical",
    "BookChapter": "Book",
    "Book": "BookSeries",
    "Dataset": "Repository",
    "JournalArticle": "Journal",
    "JournalIssue": "Journal",
    "Monograph": "Book",
    "ProceedingsArticle": "Proceedings",
    "Proceedings": "ProceedingsSeries",
    "PostedContent": "Periodical",
}

CR_TO_CM_CONTAINER_TRANSLATIONS = {
    "book": "Book",
    "book-series": "BookSeries",
    "database": "DataRepository",
    "journal": "Journal",
    "proceedings": "Proceedings",
    "periodical": "Periodical",
}

DC_TO_CM_CONTAINER_TRANSLATIONS = {
    "Book": "Book",
    "BookSeries": "BookSeries",
    "DataRepository": "DataRepository",
    "Journal": "Journal",
    "Periodical": "Periodical",
    "Proceedings": "ProceedingsSeries",
    "Repository": "Repository",
    "Series": "Series",
}

DATACITE_CONTRIBUTOR_TYPES = {
    "ContactPerson": "ContactPerson",
    "DataCollector": "DataCollector",
    "DataCurator": "DataCuration",
    "DataManager": "DataManager",
    "Distributor": "Distributor",
    "Editor": "Editor",
    "HostingInstitution": "HostingInstitution",
    "Other": "Other",
    "Producer": "Producer",
    "ProjectLeader": "ProjectLeader",
    "ProjectManager": "ProjectManager",
    "ProjectMember": "ProjectMember",
    "RegistrationAgency": "RegistrationAgency",
    "RegistrationAuthority": "RegistrationAuthority",
    "RelatedPerson": "RelatedPerson",
    "ResearchGroup": "ResearchGroup",
    "RightsHolder": "RightsHolder",
    "Researcher": "Researcher",
    "Sponsor": "Sponsor",
    "Supervisor": "Supervision",
    "WorkPackageLeader": "WorkPackageLeader",
}

# from commonmeta schema
COMMONMETA_RELATION_TYPES = [
    "IsNewVersionOf",
    "IsPreviousVersionOf",
    "IsVersionOf",
    "HasVersion",
    "IsPartOf",
    "HasPart",
    "IsVariantFormOf",
    "IsOriginalFormOf",
    "IsIdenticalTo",
    "IsTranslationOf",
    "IsReviewedBy",
    "Reviews",
    "IsPreprintOf",
    "HasPreprint",
    "IsSupplementTo",
]

# from commonmeta schema
COMMONMETA_CONTRIBUTOR_ROLES = [
    "Author",
    "Editor",
    "Chair",
    "Reviewer",
    "ReviewAssistant",
    "StatsReviewer",
    "ReviewerExternal",
    "Reader",
    "Translator",
    "ContactPerson",
    "DataCollector",
    "DataManager",
    "Distributor",
    "HostingInstitution",
    "Producer",
    "ProjectLeader",
    "ProjectManager",
    "ProjectMember",
    "RegistrationAgency",
    "RegistrationAuthority",
    "RelatedPerson",
    "ResearchGroup",
    "RightsHolder",
    "Researcher",
    "Sponsor",
    "WorkPackageLeader",
    "Conceptualization",
    "DataCuration",
    "FormalAnalysis",
    "FundingAcquisition",
    "Investigation",
    "Methodology",
    "ProjectAdministration",
    "Resources",
    "Software",
    "Supervision",
    "Validation",
    "Visualization",
    "WritingOriginalDraft",
    "WritingReviewEditing",
    "Maintainer",
    "Other",
]

INVENIORDM_IDENTIFIER_TYPES = {
    "Ark": "ark",
    "ArXiv": "arxiv",
    "Bibcode": "ads",
    "CrossrefFunderID": "crossreffunderid",
    "DOI": "doi",
    "EAN13": "ean13",
    "EISSN": "eissn",
    "GRID": "grid",
    "Handle": "handle",
    "IGSN": "igsn",
    "ISBN": "isbn",
    "ISNI": "isni",
    "ISSN": "issn",
    "ISTC": "istc",
    "LISSN": "lissn",
    "LSID": "lsid",
    "PMID": "pmid",
    "PURL": "purl",
    "UPC": "upc",
    "URL": "url",
    "URN": "urn",
    "W3ID": "w3id",
    "Other": "other",
}


CROSSREF_FUNDER_ID_TO_ROR_TRANSLATIONS = {
    "https://doi.org/10.13039/100000001": "https://ror.org/021nxhr62",
    "https://doi.org/10.13039/501100000780": "https://ror.org/00k4n6c32",
    "https://doi.org/10.13039/501100007601": "https://ror.org/00k4n6c32",
    "https://doi.org/10.13039/501100001659": "https://ror.org/018mejw64",
    "https://doi.org/10.13039/501100006390": "https://ror.org/019whta54",
    "https://doi.org/10.13039/501100001711": "https://ror.org/00yjd3n13",
    "https://doi.org/10.13039/501100003043": "https://ror.org/04wfr2810",
}


ROR_TO_CROSSREF_FUNDER_ID_TRANSLATIONS = {
    "https://ror.org/021nxhr62": "https://doi.org/10.13039/100000001",
    "https://ror.org/00k4n6c32": "https://doi.org/10.13039/501100000780",
    "https://ror.org/018mejw64": "https://doi.org/10.13039/501100001659",
    "https://ror.org/019whta54": "https://doi.org/10.13039/501100006390",
    "https://ror.org/00yjd3n13": "https://doi.org/10.13039/501100001711",
    "https://ror.org/04wfr2810": "https://doi.org/10.13039/501100003043",
}

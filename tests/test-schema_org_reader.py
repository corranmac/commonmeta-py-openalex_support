"""Test schema.org reader"""
import pytest
from talbot import Metadata
from talbot.readers.schema_org_reader import schema_org_geolocations


@pytest.mark.vcr
def test_blog_posting():
    "blog posting"
    text = "https://blog.front-matter.io/posts/eating-your-own-dog-food"
    subject = Metadata(text, via="schema_org")
    assert subject.pid == "https://doi.org/10.53731/r79vxn1-97aq74v-ag58n"
    assert subject.types == {
        "bibtex": "article",
        "citeproc": "article-newspaper",
        "resourceTypeGeneral": "Preprint",
        "ris": "GEN",
        "schemaOrg": "Article",
    }
    assert subject.url == "https://blog.front-matter.io/posts/eating-your-own-dog-food"
    assert subject.titles[0] == {"title": "Eating your own Dog Food"}
    assert len(subject.creators) == 1
    assert subject.creators[0] == {
        "name": "Martin Fenner", "nameType": "Personal"}
    assert subject.contributors is None
    assert subject.rights == [
        {
            "rights": "Creative Commons Attribution 4.0 International",
            "rightsIdentifier": "cc-by-4.0",
            "rightsIdentifierScheme": "SPDX",
            "rightsURI": "https://creativecommons.org/licenses/by/4.0/legalcode",
            "schemeUri": "https://spdx.org/licenses/",
        }
    ]
    assert subject.dates == [
        {"date": "2016-12-20", "dateType": "Issued"},
        {"date": "2022-08-15T09:06:22Z", "dateType": "Updated"},
    ]
    assert subject.publication_year == "2016"
    assert subject.publisher == "Front Matter"
    assert len(subject.related_items) == 0
    # assert subject.related_items[0] == {
    #     'relatedIdentifier': '2749-9952',
    #     'relatedIdentifierType': 'ISSN',
    #     'relationType': 'IsPartOf',
    #     'resourceTypeGeneral': 'Collection' }
    assert subject.container == {
        "identifier": "2749-9952",
        "identifierType": "ISSN",
        "title": "Front Matter",
        "type": "Blog",
    }
    assert (
        subject.descriptions[0]
        .get("description")
        .startswith("Eating your own dog food is a slang term to describe")
    )
    assert subject.subjects == [{"subject": "feature"}]
    assert subject.language == "en"
    assert subject.version is None
    assert subject.agency is None


def test_zenodo():
    "zenodo"
    text = "https://www.zenodo.org/record/1196821"
    subject = Metadata(text, via="schema_org")
    assert subject.pid == "https://doi.org/10.5281/zenodo.1196821"
    assert subject.types == {
        "bibtex": "misc",
        "citeproc": "dataset",
        "resourceTypeGeneral": "Dataset",
        "ris": "DATA",
        "schemaOrg": "Dataset",
    }
    assert subject.url == "https://zenodo.org/record/1196821"
    assert subject.titles[0] == {
        "title": (
            "PsPM-SC4B: SCR, ECG, EMG, PSR and respiration measurements in a "
            "delay fear conditioning task with auditory CS and electrical US"
        )
    }
    assert len(subject.creators) == 6
    assert subject.creators[0] == {
        "affiliation": [{"name": "University of Zurich, Zurich, Switzerland"}],
        "name": "Staib, Matthias",
        "nameType": "Personal",
    }
    assert subject.contributors is None
    assert subject.rights == [
        {
            "rights": "Creative Commons Attribution Share Alike 4.0 International",
            "rightsIdentifier": "cc-by-sa-4.0",
            "rightsIdentifierScheme": "SPDX",
            "rightsURI": "https://creativecommons.org/licenses/by-sa/4.0/legalcode",
            "schemeUri": "https://spdx.org/licenses/",
        }
    ]
    assert subject.dates == [{"date": "2018-03-14", "dateType": "Issued"}]
    assert subject.publication_year == "2018"
    assert subject.publisher == "Zenodo"
    assert len(subject.related_items) == 0
    # assert subject.related_items[0] == {
    #     'relatedIdentifier': '2749-9952',
    #     'relatedIdentifierType': 'ISSN',
    #     'relationType': 'IsPartOf',
    #     'resourceTypeGeneral': 'Collection' }
    assert subject.container == {"type": "DataRepository"}
    assert subject.funding_references is None
    assert (
        subject.descriptions[0]
        .get("description")
        .startswith("This dataset includes pupil size response")
    )
    assert subject.subjects == [
        {"subject": "pupil size response"},
        {"subject": "skin conductance response"},
        {"subject": "electrocardiogram"},
        {"subject": "electromyogram"},
        {"subject": "electrodermal activity"},
        {"subject": "galvanic skin response"},
        {"subject": "psr"},
        {"subject": "scr"},
        {"subject": "ecg"},
        {"subject": "emg"},
        {"subject": "eda"},
        {"subject": "gsr"},
    ]
    assert subject.language == "eng"
    assert subject.version == "1.0.2"
    assert subject.agency is None


def test_pangaea():
    "pangaea"
    text = "https://doi.pangaea.de/10.1594/PANGAEA.836178"
    subject = Metadata(text, via="schema_org")
    assert subject.pid == "https://doi.org/10.1594/pangaea.836178"
    assert subject.types == {
        "bibtex": "misc",
        "citeproc": "dataset",
        "resourceTypeGeneral": "Dataset",
        "ris": "DATA",
        "schemaOrg": "Dataset",
    }
    assert subject.url == "https://doi.pangaea.de/10.1594/pangaea.836178"
    assert subject.titles[0] == {
        "title": "Hydrological and meteorological investigations in a lake near Kangerlussuaq, west Greenland"
    }
    assert len(subject.creators) == 8
    assert subject.creators[0] == {
        "familyName": "Johansson",
        "givenName": "Emma",
        "nameType": "Personal",
    }
    assert subject.contributors is None
    assert subject.rights == [
        {
            "rights": "Creative Commons Attribution 3.0 Unported",
            "rightsIdentifier": "cc-by-3.0",
            "rightsIdentifierScheme": "SPDX",
            "rightsURI": "https://creativecommons.org/licenses/by/3.0/legalcode",
            "schemeUri": "https://spdx.org/licenses/",
        }
    ]
    assert subject.dates == [{"date": "2014-09-25", "dateType": "Issued"}]
    assert subject.publication_year == "2014"
    assert subject.publisher == "PANGAEA"
    assert len(subject.related_items) == 0
    # assert subject.related_items[0] == {
    #     'relatedIdentifier': '2749-9952',
    #     'relatedIdentifierType': 'ISSN',
    #     'relationType': 'IsPartOf',
    #     'resourceTypeGeneral': 'Collection' }
    assert subject.container == {
        "identifier": "https://www.pangaea.de/",
        "identifierType": "URL",
        "title": "PANGAEA",
        "type": "DataRepository",
    }
    assert (
        subject.descriptions[0]
        .get("description")
        .startswith("Few hydrological studies have been made in Greenland")
    )
    assert subject.subjects is None
    assert subject.language == "en"
    assert subject.version is None
    assert subject.geo_locations == [
        {"geoLocationPoint": {"pointLongitude": -50.18037, "pointLatitude": 67.12594}}
    ]
    assert subject.agency is None


def test_dataverse():
    "dataverse"
    text = "https://doi.org/10.7910/dvn/nj7xso"
    subject = Metadata(text, via="schema_org")
    print(subject)
    assert subject.pid == "https://doi.org/10.7910/dvn/nj7xso"
    assert subject.types == {
        "bibtex": "misc",
        "citeproc": "dataset",
        "resourceTypeGeneral": "Dataset",
        "ris": "DATA",
        "schemaOrg": "Dataset",
    }
    assert (
        subject.url
        == "https://dataverse.harvard.edu/dataset.xhtml?persistentid=doi:10.7910/dvn/nj7xso"
    )
    assert subject.titles[0] == {
        "title": "Summary data ankylosing spondylitis GWAS"}
    assert len(subject.creators) == 1
    assert subject.creators[0] == {
        "name": "International Genetics of Ankylosing Spondylitis Consortium (IGAS)"
    }
    assert subject.contributors is None
    assert subject.rights == [
        {
            "rights": "Creative Commons Zero v1.0 Universal",
            "rightsURI": "https://creativecommons.org/publicdomain/zero/1.0/legalcode",
            "rightsIdentifier": "cc0-1.0",
            "rightsIdentifierScheme": "SPDX",
            "schemeUri": "https://spdx.org/licenses/",
        }
    ]
    assert subject.dates == [
        {"date": "2017-09-30", "dateType": "Issued"},
        {"date": "2017-09-30", "dateType": "Updated"},
    ]
    assert subject.publication_year == "2017"
    assert subject.publisher == "Harvard Dataverse"
    assert len(subject.related_items) == 0
    # assert subject.related_items[0] == {
    #     'relatedIdentifier': '2749-9952',
    #     'relatedIdentifierType': 'ISSN',
    #     'relationType': 'IsPartOf',
    #     'resourceTypeGeneral': 'Collection' }
    assert subject.container == {
        "type": "DataRepository",
        "title": "Harvard Dataverse",
        "identifier": "https://dataverse.harvard.edu",
        "identifierType": "URL",
    }
    # assert subject.descriptions[0].get('description').startswith(
    #     'Summary of association tests for Nature Genetics publication')
    assert subject.subjects == [
        {"subject": "medicine, health and life sciences"},
        {"subject": " genome-wide association studies"},
        {"subject": "ankylosing spondylitis"},
    ]
    assert subject.language == "en"
    assert subject.version == "1"
    assert subject.geo_locations is None
    assert subject.agency == "Harvard Dataverse"


def test_yet_another_blog_post():
    "yet another blog post"
    text = "https://johnhawks.net/weblog/what-were-the-killing-methods-that-neandertals-used-for-large-prey-animals"
    subject = Metadata(text, via="schema_org")
    assert (
        subject.pid
        == "https://johnhawks.net/weblog/what-were-the-killing-methods-that-neandertals-used-for-large-prey-animals"
    )
    assert subject.types == {
        "bibtex": "article",
        "citeproc": "article-newspaper",
        "resourceTypeGeneral": "Preprint",
        "ris": "GEN",
        "schemaOrg": "Article",
    }
    assert (
        subject.url
        == "https://johnhawks.net/weblog/what-were-the-killing-methods-that-neandertals-used-for-large-prey-animals"
    )
    assert subject.titles[0] == {
        "title": "What killing methods enabled Neandertals to hunt large prey animals?"
    }
    assert len(subject.creators) == 1
    assert subject.creators[0] == {
        "name": "John Hawks", "nameType": "Personal"}
    assert subject.contributors is None
    assert subject.rights is None
    assert subject.dates == [
        {"date": "2022-09-24T17:22:00Z", "dateType": "Issued"},
        {"date": "2022-09-30T17:23:04Z", "dateType": "Updated"},
    ]
    assert subject.publication_year == "2022"
    assert subject.publisher == "John Hawks"
    assert len(subject.related_items) == 0
    assert subject.container == {
        "type": "Blog",
        "title": "John Hawks",
        "identifier": "https://johnhawks.net/",
        "identifierType": "URL",
    }
    assert (
        subject.descriptions[0]
        .get("description")
        .startswith("A look at sites where ancient people killed many animals")
    )
    assert subject.subjects == [
        {"subject": "neandertals"},
        {"subject": "hunter-gatherers"},
        {"subject": "hunting"},
        {"subject": "taphonomy"},
        {"subject": "technology"},
        {"subject": "cooperation"},
        {"subject": "middle paleolithic"},
    ]
    assert subject.language == "en"
    assert subject.version is None
    assert subject.geo_locations is None
    assert subject.agency is None


def test_blog_with_dois():
    "blog with dois"
    text = "https://verfassungsblog.de/einburgerung-und-ausburgerung/"
    subject = Metadata(text, via="schema_org")
    assert subject.pid == "https://doi.org/10.17176/20221210-001644-0"
    assert subject.types == {
        "bibtex": "article",
        "citeproc": "article-newspaper",
        "resourceTypeGeneral": "Preprint",
        "ris": "GEN",
        "schemaOrg": "Article",
    }
    assert subject.url == "https://verfassungsblog.de/einburgerung-und-ausburgerung"
    assert subject.titles[0] == {
        "title": "Einbürgerung und Ausbürgerung: Warum die Staatsangehörigkeitsrechtsreform nicht ohne Ausbürgerungsrechtsreform funktioniert"
    }
    assert len(subject.creators) == 1
    assert subject.creators[0] == {
        "givenName": "Maria Martha",
        "familyName": "Gerdes",
        "nameType": "Personal",
    }
    assert subject.contributors is None
    assert subject.rights is None
    assert subject.dates == [{"date": "2022-12-09", "dateType": "Issued"}]
    assert subject.publication_year == "2022"
    assert subject.publisher == "Verfassungsblog"
    assert len(subject.related_items) == 0
    assert subject.container == {"type": "Blog", "title": "Verfassungsblog"}
    assert (
        subject.descriptions[0]
        .get("description")
        .startswith(
            "Die von der Bundesinnenministerin vorangetriebene Staatsangehörigkeitsrechtsreform"
        )
    )
    assert subject.subjects == [
        {"subject": "staatsangehörigkeit"},
        {"subject": "mehrstaatigkeit"},
        {"subject": "einbürgerung"},
        {"subject": "bundesinnenministerium"},
    ]
    assert subject.language == "de-DE"
    assert subject.version is None
    assert subject.geo_locations is None
    assert subject.agency is None


def test_another_blog_with_dois():
    "another blog with dois"
    text = "https://x-dev.pages.jsc.fz-juelich.de/2022/10/05/doi-jekyll.html"
    subject = Metadata(text, via="schema_org")
    assert (
        subject.pid
        == "https://x-dev.pages.jsc.fz-juelich.de//2022/10/05/doi-jekyll.html"
    )
    assert subject.types == {
        "bibtex": "article",
        "citeproc": "post-weblog",
        "resourceTypeGeneral": "Preprint",
        "ris": "GEN",
        "schemaOrg": "BlogPosting",
    }
    assert (
        subject.url
        == "https://x-dev.pages.jsc.fz-juelich.de//2022/10/05/doi-jekyll.html"
    )
    assert subject.titles[0] == {
        "title": "DOIng it Right! (DOIs for This Blog)"}
    assert len(subject.creators) == 1
    assert subject.creators[0] == {"nameType": "Personal", "name": "Andreas"}
    assert subject.contributors is None
    assert subject.rights is None
    assert subject.dates == [
        {"date": "2022-10-05T14:35:47Z", "dateType": "Issued"},
        {"date": "2022-10-05T14:35:47Z", "dateType": "Updated"},
    ]
    assert subject.publication_year == "2022"
    assert subject.publisher == "JSC Accelerating Devices Lab"
    assert len(subject.related_items) == 0
    # assert subject.related_items[0] == {
    #     'relatedIdentifier': '2749-9952',
    #     'relatedIdentifierType': 'ISSN',
    #     'relationType': 'IsPartOf',
    #     'resourceTypeGeneral': 'Collection' }
    assert subject.container == {
        "title": "JSC Accelerating Devices Lab",
        "type": "Blog",
    }
    assert (
        subject.descriptions[0]
        .get("description")
        .startswith("1This blog is an experiment.")
    )
    assert subject.subjects is None
    assert subject.language == "en"
    assert subject.version is None
    assert subject.geo_locations is None
    assert subject.agency is None


def test_with_upstream_blog_post():
    "with upstream blog post"
    text = "https://upstream.force11.org/welcome-to-upstream/"
    subject = Metadata(text, via="schema_org")
    assert subject.pid == "https://doi.org/10.54900/rckn8ey-1fm76va-qsrnf"
    assert subject.types == {
        "bibtex": "article",
        "citeproc": "article-newspaper",
        "resourceTypeGeneral": "Preprint",
        "ris": "GEN",
        "schemaOrg": "Article",
    }
    assert subject.url == "https://upstream.force11.org/welcome-to-upstream"
    assert subject.titles[0] == {
        "title": "Welcome to Upstream: the new space for scholarly community discussion on all things open"
    }
    assert len(subject.creators) == 4
    assert subject.creators[0] == {
        "familyName": "Chodacki",
        "givenName": "John",
        "nameType": "Personal",
    }
    assert subject.contributors is None
    assert subject.rights == [
        {
            "rights": "Creative Commons Attribution 4.0 International",
            "rightsIdentifier": "cc-by-4.0",
            "rightsIdentifierScheme": "SPDX",
            "rightsURI": "https://creativecommons.org/licenses/by/4.0/legalcode",
            "schemeUri": "https://spdx.org/licenses/",
        }
    ]
    assert subject.dates == [
        {"date": "2021-11-22T05:06:00Z", "dateType": "Issued"},
        {"date": "2023-01-06T21:05:45Z", "dateType": "Updated"},
    ]
    assert subject.publication_year == "2021"
    assert subject.publisher == "Upstream"
    assert len(subject.related_items) == 0
    # assert subject.related_items[0] == {
    #     'relatedIdentifier': '2749-9952',
    #     'relatedIdentifierType': 'ISSN',
    #     'relationType': 'IsPartOf',
    #     'resourceTypeGeneral': 'Collection' }
    assert subject.container == {
        "identifier": "https://upstream.force11.org/",
        "identifierType": "URL",
        "title": "Upstream",
        "type": "Blog",
    }
    assert (
        subject.descriptions[0]
        .get("description")
        .startswith(
            "Today we are announcing Upstream. And if you’re reading this, you’re already a part of it"
        )
    )
    assert subject.subjects == [{"subject": "news"}]
    assert subject.language == "en"
    assert subject.version is None
    assert subject.geo_locations is None
    assert subject.agency is None


def test_with_blog_with_datacite_dois():
    "with blog with datacite dois"
    text = "https://blogs.tib.eu/wp/dini-ag-blog/2022/11/21/neue-standortbestimmung-fis-veroeffentlicht/"
    subject = Metadata(text, via="schema_org")
    assert (
        subject.pid
        == "https://blogs.tib.eu/wp/dini-ag-blog/2022/11/21/neue-standortbestimmung-fis-veroeffentlicht"
    )


def test_with_datacite_blog():
    "with datacite blog"
    text = "https://blog.datacite.org/investigating-pids-for-organizations-orcid-de-2-project-successfully-completed/"
    subject = Metadata(text, via="schema_org")
    assert (
        subject.pid
        == "https://blog.datacite.org/investigating-pids-for-organizations-orcid-de-2-project-successfully-completed"
    )


def test_schema_org_geolocations():
    "schema_org geolocations"
    spatial_coverage = {"spatialCoverage": {
        "@type": "Place",
        "geo": {
            "@type": "GeoCoordinates",
            "latitude": 67.12594,
            "longitude": -50.18037
        }
    }}
    none_coverage = {"spatialCoverage": None}
    assert [{'geoLocationPoint': {'pointLatitude': 67.12594,
                                  'pointLongitude': -50.18037}}] == schema_org_geolocations(spatial_coverage)
    assert None is schema_org_geolocations(none_coverage)

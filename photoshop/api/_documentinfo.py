"""Metadata about a document object.

These values can be set by selecting File > File Info in the Adobe Photoshop
application.

"""

# Import built-in modules
from pprint import pformat

# Import local modules
from photoshop.api._core import Photoshop


# pylint: disable=too-many-public-methods
class DocumentInfo(Photoshop):
    """Metadata about a document object."""

    def __init__(self, parent):
        super().__init__(parent=parent)

    def __str__(self):
        return pformat(
            {
                "author": self.author,
                "authorPosition": self.authorPosition,
                "caption": self.caption,
                "captionWriter": self.captionWriter,
                "category": self.category,
                "city": self.city,
                "country": self.country,
                "copyrightNotice": self.copyrightNotice,
                "copyrighted": self.copyrighted,
                "creationDate": self.creationDate,
                "credit": self.credit,
                "exif": self.exif,
                "headline": self.headline,
                "instructions": self.instructions,
                "jobName": self.jobName,
                "keywords": self.keywords,
                "provinceState": self.provinceState,
                "source": self.source,
                "ownerUrl": self.ownerUrl,
                "supplementalCategories": self.supplementalCategories,
                "title": self.title,
                "transmissionReference": self.transmissionReference,
                "urgency": self.urgency,
            }
        )

    @property
    def author(self):
        """str: The author."""
        return self.app.author

    @author.setter
    def author(self, name):
        self.app.author = name

    @property
    def authorPosition(self):
        """str:The author’s position."""
        return self.app.authorPosition

    @authorPosition.setter
    def authorPosition(self, name):
        self.app.authorPosition = name

    @property
    def caption(self):
        return self.app.caption

    @caption.setter
    def caption(self, name):
        self.app.caption = name

    @property
    def captionWriter(self):
        return self.app.captionWriter

    @captionWriter.setter
    def captionWriter(self, name):
        self.app.captionWriter = name

    @property
    def category(self):
        """str: The document category."""
        return self.app.category

    @category.setter
    def category(self, name):
        self.app.category = name

    @property
    def city(self):
        return self.app.city

    @city.setter
    def city(self, city_name):
        self.app.city = city_name

    @property
    def copyrightNotice(self):
        """str: The copyright notice."""
        return self.app.copyrightNotice

    @copyrightNotice.setter
    def copyrightNotice(self, name):
        self.app.copyrightNotice = name

    @property
    def copyrighted(self):
        """str: The copyright status."""
        return self.app.copyrighted

    @copyrighted.setter
    def copyrighted(self, info):
        self.app.copyrighted = info

    @property
    def country(self):
        return self.app.country

    @country.setter
    def country(self, name):
        self.app.country = name

    @property
    def creationDate(self):
        return self.app.creationDate

    @creationDate.setter
    def creationDate(self, name):
        self.app.creationDate = name

    @property
    def credit(self):
        """str: The author credit."""
        return self.app.credit

    @credit.setter
    def credit(self, value):
        self.app.credit = value

    @property
    def exif(self):
        return self.app.exif

    @exif.setter
    def exif(self, info):
        self.app.exif = info

    @property
    def headline(self):
        return self.app.headline

    @headline.setter
    def headline(self, value):
        self.app.headline = value

    @property
    def instructions(self):
        return self.app.instructions

    @instructions.setter
    def instructions(self, value):
        self.app.instructions = value

    @property
    def jobName(self):
        return self.app.jobName

    @jobName.setter
    def jobName(self, job):
        self.app.jobName = job

    @property
    def keywords(self):
        return self.app.keywords

    @keywords.setter
    def keywords(self, words):
        self.app.keywords = words

    @property
    def ownerUrl(self):
        return self.app.ownerUrl

    @ownerUrl.setter
    def ownerUrl(self, url):
        self.app.ownerUrl = url

    @property
    def provinceState(self):
        """str: The state or province."""
        return self.app.provinceState

    @provinceState.setter
    def provinceState(self, state_name):
        self.app.provinceState = state_name

    @property
    def source(self):
        return self.app.source

    @source.setter
    def source(self, source_name):
        self.app.source = source_name

    @property
    def supplementalCategories(self):
        """str: Other categories."""
        return self.app.supplementalCategories

    @supplementalCategories.setter
    def supplementalCategories(self, info):
        self.app.supplementalCategories = info

    @property
    def title(self):
        return self.app.title

    @title.setter
    def title(self, name):
        self.app.title = name

    @property
    def transmissionReference(self):
        """str: The transmission reference."""
        return self.app.transmissionReference

    @transmissionReference.setter
    def transmissionReference(self, reference):
        self.app.transmissionReference = reference

    @property
    def urgency(self):
        """The document urgency."""
        return self.app.urgency

    @urgency.setter
    def urgency(self, status):
        self.app.urgency = status

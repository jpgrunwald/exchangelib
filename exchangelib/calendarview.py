from .ewsdatetime import EWSDateTime, UTC
from .util import create_element, value_to_xml_text
from .transport import MNS


class CalendarView(object):
    XML_ELEMENT_NAME = '{%s}CalendarView' % MNS

    def __init__(self, startDate, endDate):
        self._startDate = startDate
        self._endDate = endDate

    def _date_to_xml_text(self, date):
        if isinstance(date, EWSDateTime):
            date = date.astimezone(UTC)

        return value_to_xml_text(date)

    @property
    def StartDate(self):
        return self._date_to_xml_text(self._startDate)

    @property
    def EndDate(self):
        return self._date_to_xml_text(self._endDate)

    def to_xml(self):
        return create_element(self.XML_ELEMENT_NAME,
                              StartDate=self.StartDate,
                              EndDate=self.EndDate)

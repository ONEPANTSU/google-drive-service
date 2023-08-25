from enum import Enum

from config import EVENT, TOUR, UNIVERSITY, USER


class Directory(Enum):
    EVENT = "Event"
    TOUR = "Tour"
    UNIVERSITY = "University"
    USER = "User"


directory_id = {
    Directory.EVENT: EVENT,
    Directory.TOUR: TOUR,
    Directory.UNIVERSITY: UNIVERSITY,
    Directory.USER: USER,
}

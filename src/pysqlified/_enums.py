from enum import Enum


class ExtendedEnum(Enum):
	@classmethod
	def list(cls):
		return list(map(lambda dt: dt.value, cls))

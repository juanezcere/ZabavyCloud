from dataclasses import dataclass

from ..utils.path_utils import basename, splitext


@dataclass
class File:
    """
    """
    path: str

    @property
    def filename(self) -> str:
        """

        """
        return basename(self.path)

    @property
    def ext(self) -> str:
        """
        """
        name, ext = splitext(self.filename)
        return ext[1:]


if __name__ == '__main__':
    file = File(name='test.txt', path='./data/test.txt')
    print(file)

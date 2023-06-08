import pickle
import pathlib
from abc import ABC, abstractclassmethod, abstractmethod


class BaseModel(ABC):

    # def save_file(self):
    #     info_file=pathlib.Path(self.get_file_path())
    #     if info_file.exists():

    #         with open(self.get_file_path(),'a+') as f:
                
    #             for line in self.get_file_content():
    #                 f.write(line.replace(",", ""))
    #             line=csv.writer(f)
    #     else:
    #         with open(self.get_file_path(), "a+") as f:
    #             for line in self.get_file_content():
    #                 f.write(line.replace(",", ""))
    #             line=csv.writer(f)

#for save pickle file we use this code:

    def save_file(self):
        info_file=pathlib.Path(self.get_file_path())
        if info_file.exists():
            info=self.read_pickle()

            info.append(self.get_file_content())

            with open(self.get_file_path(),'wb') as f:
                pickle.dump(info,f)

        else:
            with open(self.get_file_path(), "wb") as f:
                pickle.dump([self.get_file_content()],f)

    @abstractmethod
    def read_pickle(self) -> str:
        pass

    @abstractmethod
    def get_file_path(self):
        pass

    @abstractmethod
    def get_file_content(self) -> str:
        pass

    @classmethod
    @abstractmethod
    def from_str(cls, s: str):
        pass
    
    # @abstractmethod
    # def read_csv(self) -> str:
    #     pass

    @classmethod
    @abstractmethod
    def get_all_path(cls) -> list[str]:
        pass
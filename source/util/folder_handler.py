from pathlib import Path


class FolderHandler:
    def __init__(
        self, _main_folder: Path, _dict_folders: dict[str, bool] | None = None
    ) -> None:
        self._main_folder = _main_folder
        self._dict_folders = _dict_folders

    def get_main_folder(self) -> Path:
        return self._main_folder

    def list_sub_folders(self) -> list[str]:
        return [
            folder.name for folder in self._main_folder.iterdir() if folder.is_dir()
        ]

    def get_dict_folders(self) -> dict[str, bool] | None:
        return self._dict_folders

    def define_dictionary_sub_folders(
        self, _dict_folders: dict[str, bool] | None
    ) -> dict[str, bool]:
        if self._dict_folders is None:
            self._dict_folders = {folder: False for folder in self.list_sub_folders()}
        return self._dict_folders

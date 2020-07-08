import IPython
import os
import os.path
import pathlib
import logging

__all__ = ["see", "progress", "Path", "folder"]

logging.basicConfig(
	level=logging.INFO,
	format="%(name)-16s %(levelname)8s: %(message)s")


try:
	from see import see
except ImportError:
	logging.getLogger(__name__).warn(
		"Couldn't import `see`. Aliasing to `dir`")
	see = dir


try:
	from tqdm import tqdm as progress
except ImportError:
	logging.getLogger(__name__).warn("Couldn't import tqdm."
		" progress(...) will not show progress bars.")
	def progress(it, *args, **kwargs):
		return it

class Path(type(pathlib.Path())):
	def ls(self):
		results = []
		for child in self.iterdir():
			results.append(
				os.path.relpath(child, start=self)
					+ os.sep * child.is_dir())
		print("\n".join(sorted(results)))


folder = Path("..")
folder.data = folder/"data"
folder.data.external = folder.data/"external"
folder.data.raw = folder.data/"raw"


def _filter_available(all):
	available = lambda x: x in locals()
	return list(filter(available, all))
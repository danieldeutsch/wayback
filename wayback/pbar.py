from tqdm import tqdm


class ProgressBar(tqdm):
    """A tqdm progress bar that automatically updates the description based on
    the most recent yielded item.
    """
    def __init__(self, iterable, desc_func, **kwargs):
        super().__init__(iterable, **kwargs)
        self.desc_func = desc_func

    def __iter__(self):
        for item in super().__iter__():
            self.set_description(self.desc_func(item))
            yield item
